from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=[('EDT', 'EDT Lessons'), ('Pre-Test', 'Pre-Test Lessons'), ('Car Hire', 'Car Hire for Tests')])

    def __str__(self):
        return self.title
