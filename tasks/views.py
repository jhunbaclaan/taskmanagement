from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def dashboard(request):
    tasks = Task.objects.all()
    return render(request, "tasks/dashboard.html", {"tasks": tasks})


def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        notes = request.POST.get("notes")
        deadline = request.POST.get("deadline")
        category = request.POST.get("category")
        priority = request.POST.get("priority")

        Task.objects.create(
            title=title,
            description=description,
            notes=notes,
            deadline=deadline,
            category=category,
            priority=priority
        )
        return redirect("dashboard")
    return render(request, "tasks/create.html")


def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.title = request.POST.get("title")
        task.deadline = request.POST.get("deadline")
        task.category = request.POST.get("category")
        task.priority = request.POST.get("priority")
        task.description = request.POST.get("description")
        task.notes = request.POST.get("notes")
        task.save()
        return redirect("dashboard")
    return render(request, "tasks/create.html", {'task': task})


def complete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.completed = True
        task.save()
    return redirect("dashboard")
