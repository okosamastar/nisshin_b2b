from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="products.index"),
    path("category/", views.category, name="products.category"),
    path("detail/", views.detail, name="products.detail"),
]
