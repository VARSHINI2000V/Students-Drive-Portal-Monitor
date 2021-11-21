# Generated by Django 3.0.5 on 2021-11-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('bond', models.IntegerField(default=0)),
                ('fte', models.CharField(max_length=20)),
                ('intern', models.CharField(max_length=20)),
                ('ftepack', models.CharField(max_length=10)),
                ('internpack', models.CharField(max_length=10)),
                ('programme', models.CharField(max_length=200)),
                ('PG', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('link', models.CharField(default='NOLINK', max_length=500)),
                ('role', models.CharField(default='role', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='studentplaced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('programme', models.CharField(default='NO', max_length=100)),
                ('bond', models.IntegerField(default=0)),
                ('ftepackage', models.CharField(max_length=50)),
                ('fulltime', models.CharField(max_length=50)),
                ('intern', models.CharField(max_length=50)),
                ('internpack', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=50)),
                ('rollno', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=15)),
                ('country', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('contact', models.CharField(max_length=10)),
                ('dept', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=50)),
                ('cgpa', models.IntegerField()),
                ('backlogs', models.IntegerField(default=0)),
                ('placed', models.CharField(default='NO', max_length=20)),
            ],
        ),
    ]
