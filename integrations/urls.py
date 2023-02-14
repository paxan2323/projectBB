"""integrations URL Configuration

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
from imports.views import config_list, config_detail, config_create, config_update, config_delete
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('configs/', config_list),
    # path('configs/<int:pk>/', config_detail),
    # path('configs/create/', config_create),
    # path('configs/<int:pk>/update/', config_update),
    # path('configs/<int:pk>/delete/', config_delete),
    
    path('', config_list, name='config_list'),
    path('<int:pk>/', config_detail, name='config_detail'),
    path('create/', config_create, name='config_create'),
    path('<int:pk>/update/', config_update, name='config_update'),
    path('<int:pk>/delete/', config_delete, name='config_delete'),
]
