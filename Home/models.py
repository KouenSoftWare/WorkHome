from django.db import models

# Create your models here.


class MonitorTask(models.Model):
    task_name = models.CharField(max_length=200)
    task_host = models.CharField(max_length=200)
    task_status = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.task_host}:{self.task_name}"
