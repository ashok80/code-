"""tabledata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from tabledata.views import Home, DownloadDQFaliure, EditBHGMDock, AddBHGMDock, ViewBHGMDock, SearchLocation

urlpatterns = [
    path('', Home.as_view()),
    path('edit/<int:id>/', EditBHGMDock.as_view(), name='edit_view'),
    path('add/', AddBHGMDock.as_view(), name='add_view'),
    path('view/<int:id>/', ViewBHGMDock.as_view(), name='view_view'),
    path('search-location/', SearchLocation.as_view(), name='location-search'),
    path('dq-download/', DownloadDQFaliure.as_view()),
]
