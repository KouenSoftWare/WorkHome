from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from .models import MonitorTask
# Create your views here.


class HomeView(generic.ListView):
    template_name = 'Home/index.html'
    context_object_name = 'monitor_task_list'

    def get_queryset(self):
        return MonitorTask.objects.all()


def Home(request):
    return render(request, 'Home/index.html', {})
