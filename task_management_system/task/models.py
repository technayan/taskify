from django.db import models
import datetime
from category.models import Category

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=255)
    task_description = models.TextField()
    is_complete = models.BooleanField(default=False)
    task_assign_date = models.DateField(default=datetime.date.today)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.task_title