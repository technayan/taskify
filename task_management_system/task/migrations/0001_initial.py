# Generated by Django 4.2.7 on 2023-12-08 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=255)),
                ('taskDescription', models.TextField()),
                ('isComplete', models.BooleanField(default=False)),
                ('taskAssignDate', models.DateField(default=datetime.date.today)),
                ('category', models.ManyToManyField(to='category.category')),
            ],
        ),
    ]
