from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        name_category = ('Category')
        name_category_plural = ('Categories')       #множественное имя для Категорий

    def __str__(self):
        return self.name        # __str__ применяется для отображения объекта в интерфейсе


class TodoList(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField(blank=True)
    created_at = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))      # Дата создания
    date_end = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))        # До какой даты нужно сделать
    category = models.ForeignKey(Category, default='general', on_delete=models.CASCADE())

    class Meta:     # вспомогательный класс мета для сортировки наших дел
        ordering = ['-created']     # сортировка дел по времени их создания

    def __str__(self):
        return self.title