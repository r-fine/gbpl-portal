from django.urls import path

from .views import attendance_create_view

app_name = "attendance"
urlpatterns = [
    path('create/', view=attendance_create_view, name='create'),
]
