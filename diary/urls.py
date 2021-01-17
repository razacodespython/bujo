
from django.urls import path,include
from diary import views

urlpatterns = [
    path('', views.home, name="home"),
    path('createpost/', views.createpostmonday, name="createpost"),
    path('createpost/adjustpost/', views.createpostmonday, name="adjustpost"),
    path('createposttuesday/', views.createposttuesday, name="createposttuesday"),
    path('createposttuesday/adjustpost/', views.createposttuesday, name="adjustposttuesday")
]