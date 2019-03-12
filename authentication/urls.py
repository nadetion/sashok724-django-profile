from django.urls import include, path
from . import views

app_name = 'profile'

urlpatterns = [
     path('signup/', views.signup),
     path('login/', views.mc_login),
     path('signin/', views.signin),
     path('logout/', views.acc_logout),
     path('profile/', views.profile),
     path('uploadskin/', views.upload_skin),
     path('uploadcloak/', views.upload_cloak),
]
