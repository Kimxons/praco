from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import Lecturer

def index(request):
	lecturer_list = Lecturer.objects.all()
	context = {'lecturer_list' : lecturer_list}
	return render(request, 'mapper/index.html', context)

def detail(request, lecturer_id):
	lecturer = get_object_or_404(Lecturer, pk = lecturer_id)
	return render(request, 'mapper/detail.html', {'lecturer' : lecturer})


