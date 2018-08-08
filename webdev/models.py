from django.db import models
from purelms.models import course


# Create your models here.
class person(models.Model):
    fname=models.CharField(max_length=64)
    mname=models.CharField(max_length=64)
    lname=models.CharField(max_length=64)

    def __str__(self):
        return self.fname+" "+self.lname

class instudent(person):
    roll=models.CharField(max_length=8)
    year=models.IntegerField()
    coursestaken=models.ManyToManyField(course,related_name='course_instudents')

class outstudent(person):
    coursestaken=models.ManyToManyField(course,blank=True,related_name='course_openstudents')

class faculty(person):
    idnum=models.CharField(max_length=8)
    yremployed=models.IntegerField()
    salary=models.FloatField()
    courses=models.ManyToManyField(course,blank=True,related_name='course_faculties')

class inadmin(faculty):
    username=models.CharField(max_length=16)
    adminpasscode=models.CharField(max_length=16)

class department(models.Model):
    deptname=models.CharField(max_length=64)
    hod=models.ForeignKey(faculty,on_delete = models.CASCADE)
    coursesprovided=models.ManyToManyField(course,blank=True,related_name='dept_courses')

    def __str__(self):
        return self.deptname

class major(models.Model):
    majordegree=models.CharField(max_length=64)
    deptbelong=models.ForeignKey(department,on_delete = models.CASCADE,related_name='descipline')

    def __str__(self):
        return self.majordegree
