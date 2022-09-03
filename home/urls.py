from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.index,name='home'),
    path("home",views.home,name='home'),
    path("about",views.about,name="about"),
    path("event",views.event,name="event"),
    path("contact",views.contact,name="contact"),

]