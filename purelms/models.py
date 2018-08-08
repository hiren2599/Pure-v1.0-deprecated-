from django.db import models

# Create your models here.
class course(models.Model):
    name=models.CharField(max_length=64)
    coursecode=models.CharField(max_length=16,null=True,unique=True)
    number = models.CharField(null=True, blank=False,max_length=200)
    levelChoice=(
        ('Introductory','Introductory'),
        ('Intermediate','Intermediate'),
        ('Advanced','Advanced'),
    )
    level=models.CharField(max_length=20, choices=levelChoice, default='Introductory')
    internal_only=models.BooleanField(default=False)
    time_period = models.CharField(null=True, blank=False,max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    hidden = models.BooleanField(default=True)
    listed = models.BooleanField(default=True)
    accepts_enrollment = models.BooleanField(default=True)

    def __str__(self):
        return self.name 
