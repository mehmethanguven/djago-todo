from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from .models import Todo
# Create your views here.


def index(request):
    todos = Todo.objects.all()
    return render(request, "base.html", {"todos": todos})


@require_http_methods(["POST"])
def add(request):
    title = request.POST["title"]
    print(title)
    todo = Todo(title=title)
    todo.save()
    return redirect("index")


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.done = not todo.done
    todo.save()
    return redirect("index")

def activate(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.active = True
    todo.save()
    return redirect("index")

def deactivate(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.active = False
    todo.save()
    return redirect("index")


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")