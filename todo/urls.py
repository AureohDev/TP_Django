from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('task/edit/<int:task_id>',views.edit,name='edit'),
    path('task/done/<int:task_id>',views.done,name='done'),
    path('task/delete/<int:task_id>',views.delete,name='delete'),
]