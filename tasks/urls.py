from django.urls import path
from tasks import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("create/", views.create, name="create"),
    #path("edit/<int:task_id>/", views.edit_task, name="edit_task"),
    #path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
]


