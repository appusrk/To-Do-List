from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('sign/', views.sign, name='sign'),
    path('show/', views.show_list, name='task_list'),
    path('add/', views.add_task,name='add_to'),
    path('delete/<int:task_id>/',views.delete_task, name='del_list'),
    path('complete/<int:task_id>/',views.complete_task,name='com_task'),
]