from django.urls import path

from . import views

urlpatterns = [
    path("<str:brand>/", views.BrandView.as_view(), name="brand"),
]
