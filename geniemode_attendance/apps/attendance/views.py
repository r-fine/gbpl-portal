from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from weasyprint import HTML, CSS

from django_tables2 import SingleTableView, LazyPaginator

from .forms import AttendaceForm
from .models import Attendance
from .tables import AttendanceTable
from .utils import get_week_of_month, bulk_create_previuos_absents

import datetime
import calendar


class AttendanceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Attendance
    form_class = AttendaceForm
    success_url = reverse_lazy('home')
    success_message = 'Eentry created successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.day = datetime.datetime.now().strftime("%A")
        form.instance.date = datetime.date.today()
        form.instance.is_present = True
        form.instance.status = 'Present'

        bulk_create_previuos_absents(self, Attendance)

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_done = Attendance.objects.filter(user=self.request.user, date=datetime.datetime.now()).exists()
        context.update({
            'is_done': is_done,
            'form_title_header': 'Submit',
            'button_name': 'Submit',
            'day': datetime.datetime.now().strftime("%A"),
            'date': datetime.date.today()
        })

        return context


attendance_create_view = AttendanceCreateView.as_view()


class AttendanceUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Attendance
    form_class = AttendaceForm
    success_url = reverse_lazy('home')
    success_message = 'Entry updated successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form_title_header': 'Update',
            'button_name': 'Update',
            'day': self.object.day,
            'date': self.object.date,
        })

        return context

    def test_func(self):
        obj = self.get_object()
        if self.request.user == obj.user:
            return True
        return False


attendance_update_view = AttendanceUpdateView.as_view()


class AttendaceTableView(LoginRequiredMixin, SingleTableView):
    model = Attendance
    table_class = AttendanceTable
    template_name = "attendance/attendance_table.html"

    def get_table_data(self):
        return Attendance.objects.filter(user=self.request.user)

    def get_table_pagination(self, table):
        current_date = datetime.datetime.now()
        days_in_month = calendar.monthrange(year=current_date.year, month=current_date.month)[1]

        return {"per_page": days_in_month}


attendance_table_view = AttendaceTableView.as_view()


@login_required
def attendance_summary(request):
    current_date = datetime.datetime.now()
    current_month = current_date.month

    present_current_month = Attendance.objects.filter(
        user_id=request.user.id, date__month=current_month, status='Present',
    ).count()
    absent_current_month = Attendance.objects.filter(
        user_id=request.user.id, date__month=current_month, status='Absent',
    ).count()
    wfh_current_month = Attendance.objects.filter(
        user_id=request.user.id, date__month=current_month, work_from_home=True,
    ).count()

    context = {
        'present': present_current_month,
        'absent': absent_current_month,
        'wfh': wfh_current_month,
    }

    return render(request, 'pages/home.html', context)


@login_required
def view_pdf(request, template="attendance/pdf_template.html"):
    current_date = datetime.datetime.now()
    current_month = current_date.month

    present_current_month = Attendance.objects.filter(
        user_id=request.user.id, date__month=current_month, status='Present',
    ).count()
    absent_current_month = Attendance.objects.filter(
        user_id=request.user.id, date__month=current_month, status='Absent',
    ).count()
    wfh_current_month = Attendance.objects.filter(
        user_id=request.user.id, date__month=current_month, work_from_home=True,
    ).count()

    context = {
        'name': request.user.name,
        'department': request.user.department,
        'designation': request.user.designation,
        'phone': request.user.phone,
        'data': Attendance.objects.filter(user_id=request.user.id, date__month=current_month).order_by('created_at'),
        'month': datetime.datetime.now().strftime("%B"),
        'present': present_current_month,
        'absent': absent_current_month,
        'wfh': wfh_current_month,
    }

    pdf_html = render_to_string(template, context)
    pdf_file = HTML(string=pdf_html, base_url=request.build_absolute_uri()).write_pdf(
        stylesheets=[CSS('geniemode_attendance/static/css/bootstrap.min.css')])

    response = HttpResponse(pdf_file, content_type='application/pdf')
    filename = f"{request.user.name}_{current_date.strftime('%B')}_{current_date.strftime('%Y')}"
    response['Content-Disposition'] = "filename=%s" % (filename)

    return response
