"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('english_courses/', views.english_courses),
    path('contact/', views.contact),
    path('english_courses/babies-ages-1-2/', views.courses_babies),
    path('english_courses/kids-ages-3-8/', views.courses_kids),
    path('english_courses/preteens-ages-9-12/', views.courses_preteens),
    path('english_courses/teens-ages-13-18/', views.courses_teens),
    path('activities-english-children/', views.activities_english_children),
    path('activities-english-children/camps/', views.our_camps),
    path('activities-english-children/camps/linguistic-immersion/', views.linguistic_immersion),
    path('activities-english-children/camps/summer/', views.summer_cumps),
    path('activities-english-children/camps/sport/', views.sport_cumps),
    path('activities-english-children/camps/theme/', views.theme_cumps),
    path('activities-english-children/camps/fun-day/', views.fun_day_camps),
    path('activities-english-children/workshops', views.workshops),
    path('activities-english-children/workshops/storytime', views.storytime),
    path('activities-english-children/workshops/science', views.science),
]
