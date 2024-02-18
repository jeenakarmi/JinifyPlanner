# from django.shortcuts import render,redirect
# from django.http import HttpResponse,HttpRequest
# from .models import Todo

# def list_todo_items(request):
#     return render(request, 'todos/todo_list.html') 

# def insert_todo_item(request:HttpRequest):
#   todo = Todo(content = request.POST['content'])
#   todo.save()
#   return redirect('/todos/list/')



from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo

# Create your views here.

def list_todo_items(request):
    context = {'todo_list': Todo.objects.all() }    # pass datas from view function to template
    return render(request, 'todos/todo_list.html',context)

def insert_todo_item(request: HttpRequest): #type httpreq

    # todo is obj of model inside todo
    todo = Todo(content=request.POST['content'])    #retrieve data from content from req parameter
    todo.save()                                      # save above function
    return redirect('list_todo_items')




