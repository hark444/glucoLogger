import datetime
from django.db import models


READING_CHOICES = [
    ('FASTING', 'Fasting'),
    ('RANDOM', 'Random'),
    ('PP', 'Pp')
]


# Create your models here.
class GlucoseReadings(models.Model):
    date = models.DateField(default=datetime.datetime.now())
    reading = models.IntegerField(blank=False, null=False)
    type = models.CharField(choices=READING_CHOICES, default='FASTING', max_length=50)

    def __str__(self):
        return self.reading
