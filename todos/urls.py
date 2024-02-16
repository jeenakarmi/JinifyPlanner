# from django.urls import path
# from . import views 
# urlpatterns = [
#     path('list/',views.list_todo_items),
#     path('insert_todo/',views.insert_todo_item,name ='insert_todo_item')
# ]

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.list_todo_items, name='list_todo_items'),  # Root URL pattern
    path('list/', views.list_todo_items, name='list_todo_items'),
    path('insert_todo/', views.insert_todo_item, name='insert_todo_item'),
]




