# Generated by Django 3.0.5 on 2021-11-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0002_registeration'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeration',
            name='rollno',
            field=models.CharField(default=0, max_length=255),
        ),
    ]