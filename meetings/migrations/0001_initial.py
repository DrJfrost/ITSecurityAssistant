# Generated by Django 3.0.7 on 2020-08-09 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Price of meeting')),
                ('date', models.DateTimeField(verbose_name='Date of meeting')),
                ('description', models.TextField(verbose_name='Description of meeting')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='State of meeting')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='State of meeting')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Type of meeting')),
            ],
        ),
    ]
