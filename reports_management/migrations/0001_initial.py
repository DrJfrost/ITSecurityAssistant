# Generated by Django 3.0.6 on 2020-08-04 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meetings', '0002_auto_20200803_2244'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttackType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Is the name of the attack')),
                ('description', models.TextField(verbose_name='Is the description an attack')),
                ('risk', models.PositiveIntegerField(verbose_name='Is the risk level that has an user')),
            ],
        ),
        migrations.CreateModel(
            name='Complexity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Is the level of complexity that have an user')),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='The Operating System wich run in a PC')),
            ],
        ),
        migrations.CreateModel(
            name='ReportState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='The state of a Report')),
            ],
        ),
        migrations.CreateModel(
            name='SystemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Is a type of a system')),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='The name from the system')),
                ('description', models.TextField(verbose_name='Description of the System')),
                ('OS', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports_management.OperatingSystem')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('system_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports_management.SystemType')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='The price that you put on a report')),
                ('date', models.DateTimeField(verbose_name='The date that you did a report')),
                ('diagnostc', models.TextField(verbose_name='The final diagnostic that an expert does for aproblem')),
                ('solution', models.TextField(verbose_name='The solution that an expert does for a problem')),
                ('cve_codes', models.TextField(verbose_name='Is a code for identify a problem in cibersecurity')),
                ('analyst', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='analysis', to=settings.AUTH_USER_MODEL)),
                ('attacks', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports_management.AttackType')),
                ('auditor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reports', to=settings.AUTH_USER_MODEL)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meetings.Meeting')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports_management.ReportState')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports_management.System')),
            ],
        ),
        migrations.AddField(
            model_name='attacktype',
            name='complexity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports_management.Complexity'),
        ),
    ]
