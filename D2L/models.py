from django.db import models

# Create youfrom django.db import models

class Assignment(models.Model):
    course = models.CharField(max_length=100)
    date = models.CharField(max_length=15)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"Assignment instance with name: {self.name}, course: {self.course}, date: {self.date}"
