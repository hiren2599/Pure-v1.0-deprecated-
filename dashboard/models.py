from django.db import models
from purelms.models import course

# Create your models here.
class mycourse(models.Model):
    #remove CASCADE later
    course=models.ForeignKey(course,related_name='mycourses',on_delete=models.CASCADE,null=True)
    STATUS=(
        ('completed','completed'),
        ('incomplete','incomplete')
    )
    courseStatus=models.CharField(max_length=20,choices=STATUS,default='incomplete')

    def statuschecker(self):
        self.courseStatus='completed'

    def __str__(self):
        return self.course.name
