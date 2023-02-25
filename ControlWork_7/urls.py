"""ControlWork_7 URL Configuration

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
from book_quest.views import index, records, view_record, view_all, create_record, delete_record

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('records/', records, name='records'),
    path('view_all/', view_all, name='view_all'),
    path('create_record/', create_record, name='create_record'),

    path('view_record/<int:record_pk>', view_record, name='view_record'),
    path('record/<int:record_pk>/delete', delete_record, name='delete_record'),

]
