from django.db import models

class Lecturer(models.Model):
	pf=models.CharField(max_length=30,default="222")
	name = models.CharField(max_length=50)
	unit_name = models.CharField(null=True,max_length=50)
        
class Student(models.Model):
	reg = models.CharField(max_length=30, default="0101")
	name = models.CharField(max_length=40)
	unit_name = models.CharField(null=True, max_length=50)
   
class Unit(models.Model):
    name = models.CharField(max_length=50)
    lecturer = models.ForeignKey(Lecturer,null=True ,on_delete=models.CASCADE)
    student = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    units = models.IntegerField(default=0)

