from django.shortcuts import get_object_or_404, render
from .models import Lecturer
from django.utils import timezone
from django.http import HttpResponse

def lecturer_list(request):
	lecturers = Lecturer.objects.filter(date_joined = timezone.now()).order_by('date_joined')
	return render(request, 'mapper/lecturer.html',{'lecturers':lecturers})

