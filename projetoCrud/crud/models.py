from django.db import models

# Create your models here.
class Tarefas(models.Model):
    id = models.AutoField(primary_key=True)  
    nome = models.CharField(max_length=255, unique=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.nome