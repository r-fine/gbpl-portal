from django.db import models
from django.utils.translation import gettext_lazy as _

from geniemode_portal.apps.users.models import User


class Attendance(models.Model):

    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    day = models.CharField(_("Day"), max_length=50)

    date = models.DateField(_("Date"), auto_now=False, auto_now_add=False)

    regular_hours = models.CharField(_("Regular Hours"), max_length=50)

    in_time = models.TimeField(_("In Time"), auto_now=False, auto_now_add=False)

    out_time = models.TimeField(_("Out Time"), auto_now=False, auto_now_add=False)

    work_from_home = models.BooleanField(_("Work From Home"), default=False)

    out_office_from = models.TimeField(_("Out Office From"), auto_now=False, auto_now_add=False)

    out_office_to = models.TimeField(_("Out Office To"), auto_now=False, auto_now_add=False)

    out_reason = models.TimeField(_("Out Reason"), auto_now=False, auto_now_add=False)

    status = models.CharField(_("Status"), max_length=50)

    remarks = models.CharField(_("Remarks"), max_length=50)

    created_at = models.DateTimeField(_("Entry Created"), auto_now_add=True, editable=False)

    updated_at = models.DateTimeField(_("Entry Updated"), auto_now=True)

    is_done = models.BooleanField(_("Done"), default=False)

    class Meta:

        ordering = ['-created_at']

    def __str__(self):

        return self.user.full_name

    def get_absolute_url(self):

        return ('')

