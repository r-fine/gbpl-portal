from django import forms
from django.core.exceptions import ValidationError

from geniemode_attendance.apps.attendance.models import Attendance

import datetime


class AttendaceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ('day', 'in_time', 'out_time', 'work_from_home', 'out_office_from', 'out_office_to', 'out_reason')
        widgets = {
            'in_time': forms.TimeInput(attrs={'type': 'time', }),
            'out_time': forms.TimeInput(attrs={'type': 'time'}),
            'out_office_from': forms.TimeInput(attrs={'type': 'time'}),
            'out_office_to': forms.TimeInput(attrs={'type': 'time'}),
        }
        help_texts = {
            'in_time': 'e.g. 10:30 AM (press arrow key to toggle AM/PM)',
        }
