from django.contrib import admin

from .models import Lecturer, Student, Unit

admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Unit)