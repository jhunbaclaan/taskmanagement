from django.urls import path
from pages import views

urlpatterns = [
    path("", views.addtask, name="task"),
    path("mock2.html", views.addtask, name="task"),
    path("testFilter.html/", views.addfilter, name="filter"),
]
