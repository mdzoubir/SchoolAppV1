from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


def english_courses(request):
    return render(request, "courses/our_courses.html")


def courses_babies(request):
    return render(request, "courses/babies.html")
