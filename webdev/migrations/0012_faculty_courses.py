# Generated by Django 2.0.7 on 2018-08-05 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purelms', '0006_auto_20180804_2213'),
        ('webdev', '0011_remove_faculty_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='course_faculties', to='purelms.course'),
        ),
    ]
