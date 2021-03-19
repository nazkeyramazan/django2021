from django.db import models

# Create your models here.
class Todo_list(models.Model):
    name = models.CharField(max_length=1000 , verbose_name='Список задач')

    class Meta:
        verbose_name = "Список"
        verbose_name_plural = "Список задач "
    def __str__(self):
        return self.name

class Tasks(models.Model):
    task = models.CharField(max_length=1000, verbose_name='Название')
    created_date = models.DateField(verbose_name='Дата создания')
    due_on = models.DateField(verbose_name='Дата оканчания')
    owner = models.CharField(max_length=255, verbose_name='Владельец')
    mark = models.BooleanField(verbose_name='Статус')
    todos = models.ForeignKey(Todo_list, on_delete=models.RESTRICT, related_name='task', verbose_name='Задача')

    class Meta:
        # ordering = ['id']
        verbose_name = 'Группа'
        verbose_name_plural = 'Группа задач'