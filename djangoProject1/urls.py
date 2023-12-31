"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from app01 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # INCAR文件
    path('INCAR/list/',views.INCAR_list),
    path('INCAR/add/',views.INCAR_add),
    path('INCAR/delete/',views.INCAR_delete),
    path('INCAR/<int:nid>/edit/',views.INCAR_edit),
    path('INCAR/download/',views.INCAR_download),
    #POSCAR文件
    path('POSCAR/list/',views.POSCAR_list),
]
