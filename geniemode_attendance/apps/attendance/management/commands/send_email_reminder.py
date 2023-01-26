import datetime

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from geniemode_attendance.apps.users.models import User

from ...models import Attendance
from ...utils import get_week_of_month

current_site = Site.objects.get_current()
site_domain = current_site.domain
site_name = current_site.name


class Command(BaseCommand):
    help = "Sends an email reminder to the employees who did not entry attendance."

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        to_emails = []

        # to get email list of users who have not submitted the attendance form for the current date
        for user in users:
            # checks if Attendance object for a User for the current date exist
            if (
                Attendance.objects.filter(
                    user=user, date=datetime.date.today()
                ).exists()
                == False
            ):
                date = datetime.date.today()
                year = int(date.strftime("%Y"))
                month = int(date.strftime("%m"))
                day = int(date.strftime("%d"))
                week_of_month = get_week_of_month(year=year, month=month, day=day)
                week_day = date.strftime("%A")
                if week_day == "Saturday" and week_of_month & 1 == 1:
                    pass
                elif week_day == "Sunday":
                    pass
                else:
                    to_emails.append(user.email)

        # sends mail individually
        for email in to_emails:
            context = {
                "site_name": site_name,
                "create_attendance_url": site_domain + "/attendance/create/",
            }
            html_path = (
                str(settings.APPS_DIR) + "/templates/attendance/email_reminder.html"
            )
            msg_html = render_to_string(html_path, context)
            subject = "Attendance Reminder for " + str(datetime.date.today())
            message = ""

            if len(to_emails) != 0:
                try:
                    send_mail(
                        subject=subject,
                        message=message,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[email],
                        html_message=msg_html,
                    )
                except BaseException as e:
                    self.stdout.write(f"Problem sending email: {e}")
            self.stdout.write(
                f"send_email from: {settings.DEFAULT_FROM_EMAIL}\n to: {email}"
            )
