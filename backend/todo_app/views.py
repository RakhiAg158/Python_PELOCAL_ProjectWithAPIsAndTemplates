from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .services import fetch_all_tasks, insert_task, fetch_task_by_id, update_task, delete_task
import logging

logger = logging.getLogger(__name__)


def list_tasks(request):
    """Render tasks list page"""
    tasks = fetch_all_tasks()
    return render(request, 'index.html', {"tasks": tasks})


def add_task_page(request):
    return render(request, 'add_task.html')


@csrf_exempt
def api_get_tasks(request):
    logger.debug("Fetching all tasks")
    tasks = fetch_all_tasks()
    tasks_list = [
        {"id": t[0], "title": t[1], "description": t[2], "due_date": t[3], "status": t[4]}
        for t in tasks
    ]
    return JsonResponse(tasks_list, safe=False)


@csrf_exempt
def api_create_task(request):
    try:
        data = json.loads(request.body)
        insert_task(data["title"], data.get("description"), data.get("due_date"), data.get("status", "Pending"))
        return JsonResponse({"message": "Task created"}, status=201)
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
def api_update_task(request, task_id):
    try:
        data = json.loads(request.body)
        update_task(task_id, data["title"], data.get("description"), data.get("due_date"), data.get("status"))
        return JsonResponse({"message": "Task updated"}, status=200)
    except Exception as e:
        logger.error(f"Error updating task: {e}")
        return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
def api_delete_task(request, task_id):
    try:
        delete_task(task_id)
        return JsonResponse({"message": "Task deleted"}, status=200)
    except Exception as e:
        logger.error(f"Error deleting task: {e}")
        return JsonResponse({"error": "Invalid request"}, status=400)

def update_task_page(request, task_id):
    task = fetch_task_by_id(task_id)
    return render(request, 'update_task.html', {"task": task})

def delete_task_redirect(request, task_id):
    delete_task(task_id)
    return HttpResponseRedirect('/')
