from django.shortcuts import render
from .models import GlucoseReadings
from .forms import GlucoseReadingsForm
from django.core.paginator import Paginator
from .utils import get_trends
from django.views.decorators.http import require_GET, require_http_methods


def home(request):
    averages = get_trends(7)
    return render(request, "gluco_main/home.html", {'averages': averages})


@require_http_methods(["POST", "GET"])
def add_reading(request):
    if request.method == "GET":
        form = GlucoseReadingsForm()
        context = {'form': form}
        return render(request, "gluco_main/add_reading.html", context)
    elif request.method == "POST":
        form = GlucoseReadingsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "gluco_main/thanks.html", {})


@require_GET
def view_readings(request):
    res = GlucoseReadings.objects.all().order_by('date')
    paginator = Paginator(res, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "gluco_main/view_readings.html", {"page_obj": page_obj})
