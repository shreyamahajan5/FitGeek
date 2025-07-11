from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="health-home"),
    path('dashboard/', views.dashboard, name="health-dashboard"),
    path('tracker/', views.tracker, name="health-tracker"),
    path('appointment/', views.appointment, name="health-appointment"),
    path('picker/', views.picker, name="health-picker"),
    path('bmi/', views.bmi, name="health-bmi"),
    path('gym/', views.gym, name="health-gym"),
    path('membership/', views.membership, name="health-membership"),
    path('diet/', views.diet, name="health-diet"),
    path('signup/', views.handleSignup, name="health-signup"),
    path('login/', views.handleLogin, name="health-login"),
    path('confirmation/', views.confirmation, name="health-confirmation"),
    path('logout/', views.handleLogout, name="health-logout"),
    path('my-appointments/', views.get_appointments, name="health-my-appt"),
    path('<str:type>/exercises/', views.get_exercises, name="health-exercises"),
    path('payment/', views.payment, name="health-payment"),
    path('trainerform/', views.trainerform, name="health-trainerform"),
    path('upi/', views.upi, name="health-upi"),
    path('healthinfo/', views.healthinfo, name="health-healthinfo"),
    path('animations/', views.animations, name="health-animations"),
    path('forgetpassword/', views.forgetpassword, name="health-forgetpassword"),
    path('changepassword/', views.changepassword, name="health-changepassword"),
    path('timer/', views.timer, name="health-timer"),
    path('shop/', views.shop, name="health-shop"),
    path('gpay/', views.gpay, name="health-gpay"),
    path('obese/', views.obese, name="health-obese"),
    path('overweight/', views.overweight, name="health-overweight"),
    path('healthy/', views.healthy, name="health-healthy"),
    path('underweight/', views.underweight, name="health-underweight"),
    path('paymethods/', views.paymethods, name="health-paymethods"),
    path('healthhome/', views.healthhome, name="healthhome"),

    # ✅ Dynamic exercise route
    # Exercise Tabs
path('lungestab/', views.lungestab, name="health-lungestab"),
path('fbtab/', views.fbtab, name="health-fbtab"),
path('coretab/', views.coretab, name="health-coretab"),
path('legstab/', views.legstab, name="health-legstab"),
path('armtab/', views.armtab, name="health-armtab"),
path('backtab/', views.backtab, name="health-backtab"),
path('cardiotab/', views.cardiotab, name="health-cardiotab"),
path('shouldertab/', views.shouldertab, name="health-shouldertab"),
path('chesttab/', views.chesttab, name="health-chesttab"),

# Lunges
path('lunges/', views.lunges, name="health-lunges"),
path('reverselunges/', views.reverselunges, name="health-reverselunges"),
path('laterallunge/', views.laterallunge, name="health-laterallunge"),
path('rotationlunge/', views.rotationlunge, name="health-rotationlunge"),
path('crossbacklunge/', views.crossbacklunge, name="health-crossbacklunge"),
path('walkinglunge/', views.walkinglunge, name="health-walkinglunge"),

# Full Body
path('overheadsquat/', views.overheadsquat, name="health-overheadsquat"),
path('burpee/', views.burpee, name="health-burpee"),
path('blhcross/', views.blhcross, name="health-blhcross"),
path('pulse/', views.pulse, name="health-pulse"),
path('altopp/', views.altopp, name="health-altopp"),
path('kneehug/', views.kneehug, name="health-kneehug"),

# Cardio
path('lateralhop/', views.lateralhop, name="health-lateralhop"),
path('pulselunge/', views.pulselunge, name="health-pulselunge"),
path('hiitside/', views.hiitside, name="health-hiitside"),
path('bodyweightskip/', views.bodyweightskip, name="health-bodyweightskip"),
path('climber/', views.climber, name="health-climber"),
path('highknee/', views.highknee, name="health-highknee"),

# Core
path('abbike/', views.abbike, name="health-abbike"),
path('crunchhold/', views.crunchhold, name="health-crunchhold"),
path('coretwist/', views.coretwist, name="health-coretwist"),
path('abpulse/', views.abpulse, name="health-abpulse"),
path('legbike/', views.legbike, name="health-legbike"),
path('sidecrunch/', views.sidecrunch, name="health-sidecrunch"),

# Shoulders
path('plank/', views.plank, name="health-plank"),
path('deltraise/', views.deltraise, name="health-deltraise"),
path('frontraise/', views.frontraise, name="health-frontraise"),
path('sideplank/', views.sideplank, name="health-sideplank"),
path('armswing/', views.armswing, name="health-armswing"),
path('hippulse/', views.hippulse, name="health-hippulse"),

# Arms
path('bicepcurl/', views.bicepcurl, name="health-bicepcurl"),
path('pushpress/', views.pushpress, name="health-pushpress"),
path('seatedcurl/', views.seatedcurl, name="health-seatedcurl"),
path('dip/', views.dip, name="health-dip"),
path('crusher/', views.crusher, name="health-crusher"),
path('kickback/', views.kickback, name="health-kickback"),

# Chest
path('sprint/', views.sprint, name="health-sprint"),
path('tricep/', views.tricep, name="health-tricep"),
path('pushup/', views.pushup, name="health-pushup"),
path('decline/', views.decline, name="health-decline"),
path('incline/', views.incline, name="health-incline"),
path('modifiedpushup/', views.modifiedpushup, name="health-modifiedpushup"),

# Legs
path('highsprint/', views.highsprint, name="health-highsprint"),
path('tuckjump/', views.tuckjump, name="health-tuckjump"),
path('tempo/', views.tempo, name="health-tempo"),
path('benchjump/', views.benchjump, name="health-benchjump"),
path('splitjump/', views.splitjump, name="health-splitjump"),
path('cradle/', views.cradle, name="health-cradle"),
path('lungestab/', views.lungestab, name="health-lungestab"),

]


