from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "pages/home.html")


def contact(request):
    return render(request, "pages/contact.html")


def ec(request):
    return render(request, "pages/ec.html")


def micstore(request):
    return render(request, "pages/micstore.html")


def spring_2022(request):
    return render(request, "pages/spring_2022.html")
