from django.urls import path

from .views import (
    attendance_create_view, attendance_table_view,
)

app_name = "attendance"
urlpatterns = [
    path('create/', view=attendance_create_view, name='create'),
    path('history/', view=attendance_table_view, name='table'),
]
