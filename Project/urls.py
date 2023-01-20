"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('new',views.new),
    path('cones',views.cones),
    path('sticks',views.sticks),
    path('cake',views.cake),
    path('mochi',views.mochi),
    path('checkSearch',views.checkSearch),
    path('search',views.search),
    path('register',views.register),
    path('login',views.login),
    path('addUser',views.addUser),
    path('userLogin',views.userLogin),
    path('account',views.account),
    path('logout',views.logout),
    path('cart', views.cart),
    path('add', views.add),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('payment', views.payment),
]
