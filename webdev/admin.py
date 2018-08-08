from django.contrib import admin
from .models import person,instudent,outstudent,department,inadmin,faculty,major

# Register your models here.
admin.site.register(person)
admin.site.register(instudent)
admin.site.register(outstudent)
admin.site.register(department)
admin.site.register(inadmin)
admin.site.register(faculty)
admin.site.register(major)
