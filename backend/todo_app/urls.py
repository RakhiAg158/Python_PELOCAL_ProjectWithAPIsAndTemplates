from django.urls import path
from . import views

urlpatterns = [
    # UI Views
    path('', views.list_tasks, name='task_list'),
    path('add-task/', views.add_task_page, name='add_task'),
    path('update/<int:task_id>/', views.update_task_page, name='update_page'),
    path('delete/<int:task_id>/', views.delete_task_redirect, name='delete_page'),

    # APIs
    path('api/tasks/', views.api_get_tasks, name='api_get_tasks'),
    path('api/tasks/create/', views.api_create_task, name='api_create_task'),
    path('api/tasks/<int:task_id>/update/', views.api_update_task, name='api_update_task'),
    path('api/tasks/<int:task_id>/delete/', views.api_delete_task, name='api_delete_task'),
]
