"""
URL configuration for SAM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from agri import views
from office import views as fviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('weather/', views.weather, name='weather'),
    path('government-scheme/', views.GovermentScheme, name='government_scheme'),

    path('available-laborers/', views.AvailableLaborers, name='available_laborers'),
    path('recommend-crop/', views.RecommendCrop, name='recommend_crop'),
    path('scheme-detail/<slug:slug>/', views.schemeDetail, name='scheme_detail'),
    
    path('farmer-registration/', views.farmerRegistration, name='farmer_registration'),
    path('worker-registration/', views.workerRegistration, name='worker_registration'),


    # office login
    path('office-login/', fviews.officeLogin, name='office_login'),
    path('office-dashboard/', fviews.officeDashboard, name='office_home'),
    path('office-logout/', fviews.f_logout, name='f_logout'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
