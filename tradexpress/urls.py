"""tradexpress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from landingpage.views import landingPage
from accounts.views import getstarted_business, login, CreateUser, CreateLogin
from instantbuysell.views import instantbuysell_buy, instantbuysell_sell

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landingPage, name='landingpage'),
    path('individual/', CreateUser, name='individual'),
    path('business/', getstarted_business, name='getstarted_business'),
    path('login/', CreateLogin, name='CreateLogin'),
    path('buy/', instantbuysell_buy, name='instantbuysell_buy'),
    path('sell/', instantbuysell_sell, name='instantbuysell_sell'),
    path('login/', login, name='login'),
]
