# Generated by Django 4.0.8 on 2023-01-18 09:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0016_alter_attendance_in_time_alter_attendance_out_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
