from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.homeView.as_view(), name="home"),
    path("contact/", views.contactView.as_view(), name="contact"),
    path("ec/", views.storeView.as_view(), name="stores"),
    path("ec/micstore/", views.micstoreView.as_view(), name="micstore"),
    path("archives/", RedirectView.as_view(url="/b2b/archives/spring_2022/")),
    path("archives/<str:slug>/", views.archivePageView.as_view(), name="archive"),
    # path("special/<str:slug>/", views.landingPageView.as_view(), name="special"),
    path("healthcheck/", views.health_check),
    path("nswc/", views.welna_club),
    path("404/", views.custom_page_not_found),
]
