from django.urls import path

from . import views

# from django.views.generic import RedirectView


urlpatterns = [
    path("", views.HomeView.as_view(), name="recipe.home"),
    path("detail/<slug:slug>", views.RecipeDetail.as_view(), name="recipe.detail"),
    path("<str:cat>/", views.RecipesView.as_view(), name="recipe.recipes"),
    path("<str:cat>/<str:tag>/", views.RecipesView.as_view(), name="recipe.tags"),
]
