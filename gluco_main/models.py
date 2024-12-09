from datetime import date
from django.db import models
from django.utils import timezone


READING_CHOICES = [
    ('FASTING', 'Fasting'),
    ('RANDOM', 'Random'),
    ('PP', 'Pp')
]


# Create your models here.
class GlucoseReadings(models.Model):
    date = models.DateField(default=date.today())
    reading = models.IntegerField(blank=False, null=False)
    type = models.CharField(choices=READING_CHOICES, default='FASTING', max_length=50)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.reading
