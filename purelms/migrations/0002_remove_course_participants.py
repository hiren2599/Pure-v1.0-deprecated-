# Generated by Django 2.0.7 on 2018-08-04 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purelms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='participants',
        ),
    ]
