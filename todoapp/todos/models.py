from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=350)
    done = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
