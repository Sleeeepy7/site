from django.http import HttpResponseRedirect
from django.shortcuts import render
from . models import ToDoListItem


# Create your views here.

def todoappView(request):
    all_todo_items = ToDoListItem.objects.all()
    return render(request, 'todolist.html',
                  {'all_items': all_todo_items})


def addTodoView(request):
    x = request.POST['content']
    new_item = ToDoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todoapp')

def deleteTodoView(request, pk):
    deleteTodoView = ToDoListItem.objects.get(id=pk)
    deleteTodoView.delete()
    return HttpResponseRedirect('/todoapp')




