from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django_tables2 import SingleTableView, LazyPaginator

from .forms import AttendaceForm
from .models import Attendance
from .tables import AttendanceTable

import datetime


class AttendanceCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Attendance
    form_class = AttendaceForm
    success_url = reverse_lazy('home')
    success_message = 'Eentry created successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user
        # form.instance.day = datetime.datetime.now().strftime("%A")
        form.instance.is_present = True

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_done = Attendance.objects.filter(user=self.request.user, date=datetime.datetime.now()).exists()
        context.update({'is_done': is_done})

        return context


attendance_create_view = AttendanceCreateView.as_view()


class AttendaceTableView(SingleTableView):
    model = Attendance
    table_class = AttendanceTable
    template_name = "attendance/attendance_table.html"
    paginator_class = LazyPaginator
    table_pagination = {
        "per_page": 30
    }

    def get_table_data(self):
        return Attendance.objects.filter(user=self.request.user)


attendance_table_view = AttendaceTableView.as_view()