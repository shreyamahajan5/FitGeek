import datetime
import email
import json
import time
import uuid

import pandas as pd
import plotly
import plotly.express as px
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import redirect, render
from django.template import TemplateDoesNotExist
from newsapi import NewsApiClient

from healthproject import settings
from django.core.mail import send_mail
from .models import *

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "qBp83gL97z1g8EHhK6ipU1MZuEfEOw8J"
NEWS_API_KEY = "b52c3bd64a744b7cbb7e05e997668ecf"
APPLICATION_ID = "4d9357ff"
API_KEY = "e4171aca238375ab4d3a135d772c8a4d"
nutri_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": API_KEY,
}


def home(request):
    try:
        response = requests.get("https://zenquotes.io/api/today")
        data = response.json()
        quote = data[0].get('q', 'Stay positive!')
        author = data[0].get('a', 'Unknown')
    except Exception:
        quote = "Stay positive!"
        author = "Unknown"

    newsapi = NewsApiClient(api_key=NEWS_API_KEY)
    top_headlines = newsapi.get_top_headlines(category='health', language='en', country='in')

    news = []
    articles = top_headlines.get('articles', [])
    for article in articles[:3]:
        news.append([
            article.get('title', 'No Title'),
            article.get('description', 'No Description'),
            article.get('url', '#'),
            article.get('urlToImage', '')
        ])

    if not news:
        news.append(["No news available", "", "#", ""])

    return render(request, 'healthapp/home.html', {'news': news, 'quote': quote, 'author': author})


def exercise_view(request, exercise_name):
    template_path = f"healthapp/{exercise_name}.html"
    try:
        return render(request, template_path)
    except TemplateDoesNotExist:
        raise Http404("Exercise page not found.")


def healthhome(request): return render(request, 'healthapp/healthhome.html')
def gym(request): return render(request, 'healthapp/gym.html')
def membership(request): return render(request, 'healthapp/membership.html')
def diet(request): return render(request, 'healthapp/diet.html')
def gpay(request): return render(request, 'healthapp/gpay.html')
def shop(request): return render(request, 'healthapp/shop.html')
def timer(request): return render(request, 'healthapp/timer.html')
def picker(request): return render(request, 'healthapp/picker.html')
def trainerform(request): return render(request, 'healthapp/trainerform.html')
def animations(request): return render(request, 'healthapp/animations.html')
def confirmation(request): return render(request, 'healthapp/confirmation.html')
def upi(request): return render(request, 'healthapp/upi.html')
def payment(request): return render(request, 'healthapp/payment.html')

def obese(request): return render(request, "healthapp/obese.html")
def overweight(request): return render(request, "healthapp/overweight.html")
def healthy(request): return render(request, "healthapp/healthy.html")
def underweight(request): return render(request, "healthapp/underweight.html")

def handleSignup(request):
    if request.method == "POST":
        username = request.POST.get("name", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        if not username.isalnum():
            messages.error(request, 'Your username must only contain letters and numbers!')
            return redirect("/")
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return redirect("/")
        try:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            messages.success(request, 'Your account has been created successfully! Login Now!')
        except:
            messages.error(request, 'Your username must be unique! Please sign up again.')
        return redirect("/")
    else:
        return HttpResponseNotFound("<h1>404 - Forbidden</h1>The requested URL is not allowed!")

def handleLogin(request):
    if request.method == "POST":
        username = request.POST.get("name", "")
        password = request.POST.get("password", "")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, 'Invalid credentials!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseNotFound("<h1>404 - Forbidden</h1>The requested URL is not allowed!")

def changepassword(request): return render(request, 'healthapp/changepassword.html')
def healthinfo(request): return render(request, 'healthapp/healthinfo.html')

def forgetpassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.success(request, 'No user found with this username.')
                return redirect('/forgetpassword/')
            user_obj = User.objects.get(username=username)
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user=user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            messages.success(request, 'An email is sent.')
            return redirect('/forgetpassword/')
    except Exception as e:
        print(e)
    return render(request, 'healthapp/forgetpassword.html')

@login_required(login_url="/")
def handleLogout(request):
    if request.method == "POST":
        logout(request)
        redirect("http://127.0.0.1:8000/")
        messages.success(request, 'Successfully Logged out!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url="/")
def dashboard(request):
    if request.user.is_authenticated:
        cal_objs = Calorie.objects.filter(user=request.user).values('date', 'calorie_burnt')
        if cal_objs:
            df = pd.DataFrame(list(cal_objs))
            fig = px.bar(df, x=df['date'], y=df['calorie_burnt'], title=f"{request.user.username}'s Calorie Chart")
            graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
            return render(request, 'healthapp/dashboard.html', {'cal_objs': cal_objs, 'graph': graph})
        else:
            return render(request, 'healthapp/dashboard.html')
    return redirect("/")

def appointment(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        desc = request.POST.get('desc')
        pincode = request.POST.get('pincode')
        appointment = Appointment.objects.create(user=request.user, full_name=full_name, email=email, phone=phone,
                                                 desc=desc, address=address, pincode=pincode)
        appointment.save()
        messages.success(request, "Your appointment has been booked successfully!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'healthapp/appointment.html')

@login_required(login_url="/")
def get_appointments(request):
    if request.user.is_authenticated:
        my_appointments = Appointment.objects.filter(user=request.user)
        return render(request, "healthapp/my_appointments.html", {'my_appt': my_appointments})
    return redirect("/")

@login_required(login_url="/")
def bmi(request):
    if request.method == "POST":
        weight = float(request.POST.get("weight"))
        height = float(request.POST.get("height"))
        bmi = int((weight / (height ** 2)) * 10000)
        if bmi < 18.5:
            text = "warning"
            remarks = "Underweight"
        elif 18.5 <= bmi < 25:
            text = "success"
            remarks = "Healthy"
        elif 25 <= bmi < 30:
            text = "warning"
            remarks = "Overweight"
        elif 30 <= bmi < 35:
            text = "warning"
            remarks = "Obese"
        else:
            text = "danger"
            remarks = "Extremely Obese."
        return render(request, "healthapp/bmi.html", {'bmi': bmi, 'text': text, 'remarks': remarks})
    return render(request, "healthapp/bmi.html")

@login_required(login_url="/")
def tracker(request):
    if request.user.is_authenticated:
        done = True
        user_prev_cal = Calorie.objects.filter(user=request.user).order_by("-date")
        if user_prev_cal:
            prev_date = user_prev_cal[0].date
            date_today = datetime.datetime.now().date()
            if date_today > prev_date:
                done = False
        else:
            done = False
        if request.method == "POST":
            cal = float(request.POST.get("cal", "0"))
            if not cal:
                exercise_params = {
                    "query": request.POST.get("calnlp", ""),
                    "gender": "male",
                    "weight_kg": request.POST.get("weight", "0"),
                    "height_cm": request.POST.get("height", "0"),
                    "age": int(request.POST.get("age", "0"))
                }
                query = requests.post(url=nutri_api_endpoint, json=exercise_params, headers=headers)
                data = query.json()
                total_cal_burnt = 0
                total_mins_spent = 0
                for exercise in data['exercises']:
                    total_cal_burnt += exercise['nf_calories']
                    total_mins_spent += exercise['duration_min']
                cal_obj = Calorie.objects.create(calorie_burnt=total_cal_burnt, user=request.user)
                cal_obj.save()
                done = True
                messages.info(request, f"You've burnt {total_cal_burnt} calories and spent {total_mins_spent} minutes!")
                return render(request, 'healthapp/tracker.html', {'done': "true"})
            if not done:
                cal_obj = Calorie.objects.create(calorie_burnt=cal, user=request.user)
                cal_obj.save()
                messages.success(request, "Your calories for today has been recorded!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if done:
            return render(request, 'healthapp/tracker.html', {'done': "true"})
    else:
        return redirect("/")
    return render(request, 'healthapp/tracker.html')

def get_exercises(request, type):
    exercises = Exercise.objects.filter(type=type)
    return render(request, "healthapp/exercises.html", {'exercises': exercises, 'type': type})
def paymethods(request):
    return render(request, 'healthapp/paymethods.html')

def exercise_view(request, exercise_name):
    template_path = f"healthapp/{exercise_name}.html"
    try:
        return render(request, template_path)
    except TemplateDoesNotExist:
        raise Http404("Exercise page not found.")



# Tabs and Exercises

def lunges(request): return render(request, "healthapp/lunges.html")
def reverselunges(request): return render(request, "healthapp/reverselunges.html")
def laterallunge(request): return render(request, "healthapp/laterallunge.html")
def rotationlunge(request): return render(request, "healthapp/rotationlunge.html")
def crossbacklunge(request): return render(request, "healthapp/crossbacklunge.html")
def walkinglunge(request): return render(request, "healthapp/walkinglunge.html")

def overheadsquat(request): return render(request, "healthapp/overheadsquat.html")
def burpee(request): return render(request, "healthapp/burpee.html")
def blhcross(request): return render(request, "healthapp/blhcross.html")
def pulse(request): return render(request, "healthapp/pulse.html")
def altopp(request): return render(request, "healthapp/altopp.html")
def kneehug(request): return render(request, "healthapp/kneehug.html")

def lateralhop(request): return render(request, "healthapp/lateralhop.html")
def pulselunge(request): return render(request, "healthapp/pulselunge.html")
def hiitside(request): return render(request, "healthapp/hiitside.html")
def bodyweightskip(request): return render(request, "healthapp/bodyweightskip.html")
def climber(request): return render(request, "healthapp/climber.html")
def highknee(request): return render(request, "healthapp/highknee.html")

def abbike(request): return render(request, "healthapp/abbike.html")
def crunchhold(request): return render(request, "healthapp/crunchhold.html")
def coretwist(request): return render(request, "healthapp/coretwist.html")
def abpulse(request): return render(request, "healthapp/abpulse.html")
def legbike(request): return render(request, "healthapp/legbike.html")
def sidecrunch(request): return render(request, "healthapp/sidecrunch.html")

def plank(request): return render(request, "healthapp/plank.html")
def deltraise(request): return render(request, "healthapp/deltraise.html")
def frontraise(request): return render(request, "healthapp/frontraise.html")
def sideplank(request): return render(request, "healthapp/sideplank.html")
def armswing(request): return render(request, "healthapp/armswing.html")
def hippulse(request): return render(request, "healthapp/hippulse.html")

def bicepcurl(request): return render(request, "healthapp/bicepcurl.html")
def pushpress(request): return render(request, "healthapp/pushpress.html")
def seatedcurl(request): return render(request, "healthapp/seatedcurl.html")
def dip(request): return render(request, "healthapp/dip.html")
def crusher(request): return render(request, "healthapp/crusher.html")
def kickback(request): return render(request, "healthapp/kickback.html")

def sprint(request): return render(request, "healthapp/sprint.html")
def tricep(request): return render(request, "healthapp/tricep.html")
def pushup(request): return render(request, "healthapp/pushup.html")
def decline(request): return render(request, "healthapp/decline.html")
def incline(request): return render(request, "healthapp/incline.html")
def modifiedpushup(request): return render(request, "healthapp/modifiedpushup.html")
def lungestab(request): return render(request, "healthapp/lungestab.html")
def fbtab(request): return render(request, "healthapp/fbtab.html")
def coretab(request): return render(request, "healthapp/coretab.html")
def legstab(request): return render(request, "healthapp/legstab.html")
def armtab(request): return render(request, "healthapp/armtab.html")
def backtab(request): return render(request, "healthapp/backtab.html")
def cardiotab(request): return render(request, "healthapp/cardiotab.html")
def shouldertab(request): return render(request, "healthapp/shouldertab.html")
def chesttab(request): return render(request, "healthapp/chesttab.html")
def highsprint(request): return render(request, "healthapp/highsprint.html")
def tuckjump(request): return render(request, "healthapp/tuckjump.html")
def tempo(request): return render(request, "healthapp/tempo.html")
def benchjump(request): return render(request, "healthapp/benchjump.html")
def splitjump(request): return render(request, "healthapp/splitjump.html")
def cradle(request): return render(request, "healthapp/cradle.html")

def exercise_view(request, exercise_name):
    raise Http404("Dynamic exercise routing is disabled.")
