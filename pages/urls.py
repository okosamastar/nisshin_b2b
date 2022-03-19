from django.urls import path

from . import views

urlpatterns = [
    path("", views.homeView.as_view(), name="home"),
    path("contact/", views.contactView.as_view(), name="contact"),
    path("ec/", views.storestView.as_view(), name="stores"),
    path("ec/micstore/", views.storestView.as_view(), name="store"),
    path("spring_2022/", views.spring_2022, name="spring_2022"),
]
