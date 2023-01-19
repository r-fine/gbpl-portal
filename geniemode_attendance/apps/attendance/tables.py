from django.utils.safestring import mark_safe

from .models import Attendance

import django_tables2 as tables


class AttendanceTable(tables.Table):
    updatable = {
        'td': {'data-href': lambda record: record.get_update_url}
    }
    update = tables.Column(
        attrs=updatable,
        default=mark_safe(
            '''
            <button class="btn btn-sm">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                    <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                    <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
                </svg>
            </button>
            '''
        )
    )
    date = tables.Column(orderable=True)
    # created_at = tables.Column(orderable=True)

    class Meta:
        model = Attendance
        tempplate_name = 'django_tables2/bootstrap4.html'
        fields = (
            'day', 'date', 'in_time', 'out_time', 'work_from_home', 'out_office_from', 'out_office_to', 'out_reason', 'status', 'remarks', 'update',
        )
        attrs = {
            'class': 'table table-striped table-hover',
            'id': 'myTable',
        }
        orderable = False
    #     order_by = 'created_at'

    # def before_render(self, request):
    #     """
    #     A way to hook into the moment just before rendering the template.
    #     Can be used to hide a column.
    #     """
    #     return self.columns.hide('created_at')
