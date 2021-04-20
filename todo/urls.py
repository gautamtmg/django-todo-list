from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create_todo, name='create-todo'),
    path('todo/<int:id>', views.detail, name='todo'),
    path('todo-delete/<int:id>/', views.todo_delete, name="todo-delete"),
    path('todo-edit/<int:id>/', views.todo_edit, name="todo-edit"),
]