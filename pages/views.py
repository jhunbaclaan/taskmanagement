from django.shortcuts import render

def addtask(request):
    return render(request, "pages/addtask.html", {})

def addfilter(request):
    return render(request, "pages/addfilter.html", {})
