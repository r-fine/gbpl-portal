import datetime
import calendar
import numpy as np

calendar.setfirstweekday(6)


def get_week_of_month(year, month, day):
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x == day)[0][0] + 1

    return (week_of_month)


def bulk_create_previuos_absents(self, model):
    previous = model.objects.filter(user=self.request.user).order_by(
        '-id')[0] if model.objects.filter(user=self.request.user).exists() else None
    if previous:
        previous_date = previous.date
        current_date = datetime.date.today()
        diff = current_date - previous_date
        days_diff = diff.days  # type: int
        for i in range(days_diff-1, 0, -1):
            date = datetime.date.today() - datetime.timedelta(days=i)
            year = int(date.strftime("%Y"))
            month = int(date.strftime("%m"))
            day = int(date.strftime("%d"))
            week_of_month = get_week_of_month(year=year, month=month, day=day)
            week_day = date.strftime("%A")
            if week_day == 'Saturday' and week_of_month & 1 == 1:  # check if week_of_month is odd
                data = model.objects.create(
                    user=self.request.user, day=week_day, date=date,
                    in_time=None, out_time=None,
                    status='Weekend',
                )
                data.save()
            elif week_day == 'Sunday':
                data = model.objects.create(
                    user=self.request.user, day=week_day, date=date,
                    in_time=None, out_time=None,
                    status='Weekend',
                )
                data.save()
            else:
                data = model.objects.create(
                    user=self.request.user, day=week_day, date=date,
                    in_time=None, out_time=None,
                    status='Absent',
                )
                data.save()
