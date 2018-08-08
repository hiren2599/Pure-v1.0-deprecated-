# Generated by Django 2.0.7 on 2018-07-31 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webdev', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='webdev.person')),
                ('roll', models.IntegerField()),
            ],
            bases=('webdev.person',),
        ),
    ]
