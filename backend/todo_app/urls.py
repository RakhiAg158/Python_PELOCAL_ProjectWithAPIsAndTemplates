from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks, name='task_list'),
]
