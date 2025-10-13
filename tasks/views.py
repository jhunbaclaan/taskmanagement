from django.shortcuts import render, redirect
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


