from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def english_courses(request):
    return render(request, "courses/our_courses.html")


def courses_babies(request):
    return render(request, "courses/babies.html")

def courses_kids(request):
    return render(request, "courses/kids.html")


def courses_preteens(request):
    return render(request, "courses/preteens.html")


def courses_teens(request):
    return render(request, "courses/teens.html")
