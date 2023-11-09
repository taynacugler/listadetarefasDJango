from django.contrib import admin
from django.urls import path
from .views import getTarefas, createTarefa, updateTarefa, update, delete, checkedTarefa

urlpatterns = [
path('', getTarefas, name='getTarefas'),
path('createTarefa/', createTarefa, name='createTarefa'),
path('updateTarefa/<int:id>', updateTarefa, name='updateTarefa'),
path('checkedTarefa/<int:id>', checkedTarefa, name='checkedTarefa'),
path('update/<int:id>', update, name='update'),
path('delete/<int:id>', delete, name='delete'),

]