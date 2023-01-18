from .models import Attendance

import django_tables2 as tables


class AttendanceTable(tables.Table):
    class Meta:
        model = Attendance
        tempplate_name = 'django_tables2/bootstrap4.html'
        fields = (
            'id', 'day', 'date', 'in_time', 'out_time', 'work_from_home', 'out_office_from', 'out_office_to', 'out_reason', 'status', 'remarks',
        )
        attrs = {
            'class': 'table table-striped table-hover',
            'id': 'myTable',
        }
        order_by = 'id'

    def before_render(self, request):
        """
        A way to hook into the moment just before rendering the template.
        Can be used to hide a column.
        """
        return self.columns.hide('id')
