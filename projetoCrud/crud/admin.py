from django.contrib import admin
from .models import Tarefas, checkedTarefas

# Register your models here.
admin.site.register(Tarefas)
admin.site.register(checkedTarefas)