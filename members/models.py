from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    join_date = models.DateField(auto_now_add=True)
    total_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
