from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password_hash = models.CharField(max_length=128)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
