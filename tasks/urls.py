from django.urls import path
from tasks import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("create/", views.create, name="create"),
    path("delete/<int:id>/", views.delete_task, name="delete_task"),
    path("update/<int:pk>/", views.update_task, name="update_task"),
    path("duplicate/<int:task_id>/", views.duplicate_task, name="duplicate_task"),
    path("toggle_complete/<int:id>/", views.toggle_complete, name="toggle_complete"),

]


