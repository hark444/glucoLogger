# from datetime import timezone
from django.forms import ModelForm
from .models import GlucoseReadings
from django.forms import SelectDateWidget


class GlucoseReadingsForm(ModelForm):
    class Meta:
        model = GlucoseReadings
        fields = "__all__"
        widgets = {
            'date': SelectDateWidget()
        }
