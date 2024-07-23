from django.db.models import Avg
from .models import GlucoseReadings


def get_trends(records: int = 7) -> dict:
    # Getting avg value for all sugar types for last #records, default: last 7 records
    fasting_avg = GlucoseReadings.objects.filter(type='FASTING').order_by('-id')[:records].aggregate(Avg('reading'))
    random_avg = GlucoseReadings.objects.filter(type='RANDOM').order_by('-id')[:records].aggregate(Avg('reading'))
    pp_avg = GlucoseReadings.objects.filter(type='PP').order_by('-id')[:records].aggregate(Avg('reading'))

    fasting_avg_round = f"{fasting_avg.get('reading__avg'):.2f}" if fasting_avg.get('reading__avg') else None
    random_avg_round = f"{random_avg.get('reading__avg'):.2f}" if random_avg.get('reading__avg') else None
    pp_avg_round = f"{pp_avg.get('reading__avg'):.2f}" if pp_avg.get('reading__avg') else None

    return {'fasting_avg': fasting_avg_round, 'random_avg': random_avg_round, 'pp_avg': pp_avg_round}
