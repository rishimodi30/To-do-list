from unicodedata import name
from django import views
from django.urls import URLPattern, path
from . import views
urlpatterns = [
  
  path('',views.index,name='index'),
  path('update_task/<str:pk>/',views.updateTask,name="update_task"),
  path('delete/<str:pk>/',views.deleteTask,name="delete"),

]