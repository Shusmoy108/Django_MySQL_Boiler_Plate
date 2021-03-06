"""Django_MySQL_Boiler_Plate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Django_MySQL_Boiler_Plate.views import hello,templateexample, appointment,login,ModuleAdd

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('template/', templateexample),
    path('appointment/', appointment,name='appointment'),
    # path('submit/', logindata),
    path('login/', login),
    path('add/',ModuleAdd,name='ModuleAdd'),
    # path('login/', login),
]
