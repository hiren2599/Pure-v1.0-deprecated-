# Generated by Django 2.0.7 on 2018-08-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mycourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseStatus', models.CharField(choices=[('completed', 'completed'), ('incomplete', 'incomplete')], default='incomplete', max_length=20)),
            ],
        ),
    ]
