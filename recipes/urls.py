from django.urls import path

from . import views

# from django.views.generic import RedirectView


urlpatterns = [
    # path("", views.CategoriesView.as_view(), name="recipes.top"),
    path("detail/<slug:slug>", views.RecipeDetail.as_view(), name="recipe.detail"),
]
