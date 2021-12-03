from django.http import request
from django.shortcuts import redirect, render
from .models import Todo

# Create your views here.

def index(request):
    todo = Todo.objects.all()
    
    if request.method == 'POST':
        new_items = Todo(
            items = request.POST['items']
        )   
        new_items.save()
        
        return redirect('/')

    return render(request, 'index.html', {'todos': todo})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()

    return redirect('/')
    