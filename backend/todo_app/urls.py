from django.urls import path
from . import views

urlpatterns = [
    # Template pages
    path('', views.list_tasks, name='task_list'),
    path('add-task/', views.add_task_page, name='add_task'),

    # API endpoints
    path('api/tasks/', views.api_get_tasks, name='api_get_tasks'),
    path('api/tasks/create/', views.api_create_task, name='api_create_task'),
    path('api/tasks/<int:task_id>/update/', views.api_update_task, name='api_update_task'),
    path('api/tasks/<int:task_id>/delete/', views.api_delete_task, name='api_delete_task'),
]
