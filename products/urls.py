from django.urls import path

from . import views

urlpatterns = [
    path("", views.CategoriesView.as_view(), name="products.category"),
    path("detail/<slug:slug>", views.ProductDetail.as_view(), name="products.detail"),
    path("<str:cat>/", views.ProductsView.as_view(), name="products.products"),
    path(
        "<str:cat>/<str:child>", views.ProductsView.as_view(), name="products.products"
    ),
    path("<str:cat>/<str:tag>/", views.ProductsView.as_view(), name="products.tags"),
]
