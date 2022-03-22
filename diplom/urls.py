"""diplom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from classroom import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ShowAll.as_view(), name='show_all'),
    path('check/', views.CheckView.as_view(), name='check'),
    path('show_konspect/', views.ShowKonspectView.as_view(), name='show_konspect'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('material/<int:material_id>', views.MaterialView.as_view(), name='show_material'),
    path('questions_konspect/<int:material_id>', views.QuestionsKonspectView.as_view(), name='questions_konspect'),
    path('itog_konspect/', views.ItogKonspectView.as_view(), name='itog_konspect'),
    path('all_tests/', views.AllTestsView.as_view(), name='all_tests'),
    path('show_test/<int:test_id>', views.ShowTestView.as_view(), name='show_test'),
]
