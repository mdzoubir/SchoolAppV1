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
    path('english_courses/babies-ages-1-2/', views.courses_babies),
    path('english_courses/kids-ages-3-8/', views.courses_kids),
    path('english_courses/preteens-ages-9-12/', views.courses_preteens),
    path('english_courses/teens-ages-13-18/', views.courses_teens),
]
