# Generated by Django 4.0.8 on 2023-01-10 22:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=50, verbose_name='Day')),
                ('date', models.DateField(verbose_name='Date')),
                ('regular_hours', models.CharField(max_length=50, verbose_name='Regular Hours')),
                ('in_time', models.TimeField(verbose_name='In Time')),
                ('out_time', models.TimeField(verbose_name='Out Time')),
                ('work_from_home', models.BooleanField(default=False, verbose_name='Work From Home')),
                ('out_office_from', models.TimeField(verbose_name='Out Office From')),
                ('out_office_to', models.TimeField(verbose_name='Out Office To')),
                ('out_reason', models.TimeField(verbose_name='Out Reason')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
                ('remarks', models.CharField(max_length=50, verbose_name='Remarks')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Entry Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Entry Updated')),
                ('is_present', models.BooleanField(default=False, verbose_name='Done')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
