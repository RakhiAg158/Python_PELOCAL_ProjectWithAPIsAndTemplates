from django.http import HttpResponse

def list_tasks(request):
    return HttpResponse("Task List Page - View works!")
