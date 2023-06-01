"""blackshoes URL Configuration

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
from django.conf.urls import include 
from option_calculator.views import two_step
from option_calculator.views import n_step
from option_calculator.views import black_scholes
from option_calculator.views import home_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('two steps', two_step),
    path('n steps', n_step),
    path('black scholes', black_scholes),
]
