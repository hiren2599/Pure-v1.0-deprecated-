# Generated by Django 2.0.7 on 2018-07-31 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=64)),
                ('mname', models.CharField(max_length=64)),
                ('lname', models.CharField(max_length=64)),
            ],
        ),
    ]
