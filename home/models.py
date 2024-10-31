from django.db import models

class Lesson(models.Model):
    CATEGORY_CHOICES = [
        ('EDT', 'EDT Lessons'),
        ('Pre-Test', 'Pre-Test Lessons'),
        ('Car Hire', 'Car Hire for Tests')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    transmission = models.CharField(max_length=20, choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')])
    preferred_start_date = models.DateField(null=True, blank=True)
    test_booked = models.BooleanField(default=False)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title