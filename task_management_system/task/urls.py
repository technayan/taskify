from django.urls import path
from .views import addTask, editTask, deleteTask

urlpatterns = [
    path('add_task/', addTask, name = "add_task"),
    path('edit_task/<int:id>/', editTask, name = "edit_task"),
    path('delete_task/<int:id>/', deleteTask, name = "delete_task")
]
