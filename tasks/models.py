from django.db import models


class Task(models.Model):
    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Social', 'Social'),
        ('Financial', 'Financial'),
        ('School', 'School'),
        ('Health', 'Health'),
    ]

    PRIORITY_CHOICES = [
        ('One', 'One (High)'),
        ('Two', 'Two'),
        ('Three', 'Three'),
        ('Four', 'Four'),
        ('Five', 'Five (Low)'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    notes = models.TextField(blank=True, null=True)
    deadline = models.DateField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

