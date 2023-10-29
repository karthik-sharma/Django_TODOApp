from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('main_page/', views.main_page, name='main_page'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]
