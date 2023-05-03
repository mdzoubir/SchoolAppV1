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


def activities_english_children(request):
    return render(request, "activities/our_activities.html")


def our_camps(request):
    return render(request, "activities/camps/our_camps.html")


def linguistic_immersion(request):
    return render(request, "activities/camps/linguistic_immersion.html")


def summer_cumps(request):
    return render(request, "activities/camps/summer.html")


def sport_cumps(request):
    return render(request, "activities/camps/sport.html")