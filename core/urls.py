from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('update/<int:item_id>/', views.update_todo, name='update_todo'),
    path('delete/<int:item_id>/', views.delete_todo, name='delete_todo'),
]