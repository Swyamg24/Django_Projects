# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

def todo_list(request):
    items = TodoItem.objects.all().order_by('-created_at')
    return render(request, 'todo/index.html', {'items': items})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        TodoItem.objects.create(title=title)
    return redirect('todo_list')

def update_todo(request, item_id):
    item = get_object_or_404(TodoItem, id=item_id)
    item.completed = not item.completed
    item.save()
    return redirect('todo_list')

def delete_todo(request, item_id):
    item = get_object_or_404(TodoItem, id=item_id)
    item.delete()
    return redirect('todo_list')