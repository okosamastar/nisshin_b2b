from django.urls import path

from . import views

urlpatterns = [
    path("", views.homeView.as_view(), name="home"),
    path("contact/", views.contactView.as_view(), name="contact"),
    path("ec/", views.storeView.as_view(), name="stores"),
    path("ec/micstore/", views.micstoreView.as_view(), name="micstore"),
    # path("spring_2022/", views.spring_2022, name="spring_2022"),
    path("404/", views.custom_page_not_found),
]
