from django.urls import path

from .views import (
    attendance_create_view,
    attendance_table_view,
    attendance_update_view,
    view_pdf,
)

app_name = "attendance"
urlpatterns = [
    path("create/", view=attendance_create_view, name="create"),
    path("update/<uuid:pk>/", view=attendance_update_view, name="update"),
    path("history/", view=attendance_table_view, name="table"),
    path("pdf-view/", view=view_pdf, name="view_pdf"),
]
