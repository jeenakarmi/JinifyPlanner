# from django.urls import path
# from . import views 
# urlpatterns = [
#     path('list/',views.list_todo_items),
#     path('insert_todo/',views.insert_todo_item,name ='insert_todo_item')
# ]

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.list_todo_items, name='list_todo_items'),  # Root URL pattern #entry point for accessing list of todo items within web application.
    # path('list/', views.list_todo_items, name='list_todo_items'), # to access a list of todo items
    path('insert_todo/', views.insert_todo_item, name='insert_todo_item'),  #to handle inserting new todo items

    #pass value of  int todo_id from view
    path('delete_todo/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item'), #route for delete
]




