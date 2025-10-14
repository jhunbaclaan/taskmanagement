from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST
import json
from .models import Task


def dashboard(request):
    tasks = Task.objects.all()
    return render(request, "tasks/dashboard.html", {"tasks": tasks})


def create(request, id=None):
    task = None

    # If there's an ID, we're editing an existing task
    if id:
        task = get_object_or_404(Task, id=id)

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        notes = request.POST.get("notes")
        deadline = request.POST.get("deadline")
        category = request.POST.get("category")
        priority = request.POST.get("priority")

        if task:
            # ✅ Update existing task
            task.title = title
            task.description = description
            task.notes = notes
            task.deadline = deadline
            task.category = category
            task.priority = priority
            task.save()
        else:
            # ✅ Create a new task
            Task.objects.create(
                title=title,
                description=description,
                notes=notes,
                deadline=deadline,
                category=category,
                priority=priority
            )

        return redirect("dashboard")

    # If it's GET, load create.html — with task data if editing
    return render(request, "tasks/create.html", {"task": task})



def delete_task(request, id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=id)
        task.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Invalid request"}, status=400)

def update_task(request, pk):
    task = get_object_or_404(Task, pk = pk)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.deadline = request.POST.get("deadline")
        task.category = request.POST.get("category")
        task.priority = request.POST.get("priority")
        task.description = request.POST.get("description")
        task.notes = request.POST.get("notes")
        task.save()
        return redirect("dashboard")

def duplicate_task(request, task_id):
    if request.method == "POST":
        try:
            original = Task.objects.get(id=task_id)
            new_task = Task.objects.create(
                title=f"{original.title} (Copy)",
                description=original.description,
                notes=original.notes,
                category=original.category,
                priority=original.priority,
                deadline=original.deadline,
            )
            new_task.save()
            return JsonResponse({"status": "success"})
        except Task.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Task not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)

@require_POST
@csrf_protect
def toggle_complete(request, id):
    task = Task.objects.get(id=id)
    data = json.loads(request.body)
    task.completed = data.get("completed", False)
    task.save()
    return JsonResponse({"success": True})
    
