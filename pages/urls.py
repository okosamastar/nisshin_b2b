from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("ec/", views.ec, name="ec"),
    path("ec/micstore/", views.micstore, name="micstore"),
    path("spring_2022/", views.spring_2022, name="spring_2022"),
]
