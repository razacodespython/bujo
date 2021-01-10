
from django.urls import path,include
from diary import views

urlpatterns = [
    path('', views.home, name="home"),
    path('createpost/', views.createpost, name="createpost"),
    path('createpost/adjustpost/', views.createpost, name="adjustpost")
   
]