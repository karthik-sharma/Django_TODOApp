from django.db import models

# Create your models here.

class TODOList(models.Model):
    done = models.BooleanField(null=True, default=False)
    task = models.TextField(max_length=1000, null=True)
    due_date = models.DateField(null=True)
    priority = models.CharField(max_length=50, null=True)

    