from datetime import date, time, datetime, timedelta

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from web.models import Quotation, Client, Appointment, Payment

class FreeHours(APIView):
    """
    list of available hours by date
    """
    def get(self, request, *args, **kwargs):
        import pytz
        utc=pytz.UTC
        date = kwargs.get('date')
        events =Appointment.objects.filter(dia=date)
        if events:
            appointments = []
            for event in events:
                start_date = datetime.combine(event.dia, event.start)
                start_date = utc.localize(start_date)
                end_date = datetime.combine(event.dia, event.end)
                end_date = utc.localize(end_date)
                appointments.append((start_date, end_date))
            year, month,day = date.split('-')
            work_hours = (datetime(int(year), int(month), int(day), 11, tzinfo=utc),
                datetime(int(year), int(month), int(day), 18, tzinfo=utc))
            work_intervals = timedelta(minutes=30)
            slots = sorted([(work_hours[0], work_hours[0])] + appointments + [(work_hours[1], work_hours[1])])
            free_hours = []
            for start, end in ((slots[i][1], slots[i+1][0]) for i in range(len(slots)-1)):
                assert start <= end, "Cannot attend all appointments"
                while start + work_intervals <= end:
                    free_hours.append("{:%H:%M}".format(start))
                    start += work_intervals
            return Response(free_hours)
        else:
            horas = ["11:00", "11:30", "12:00",
                "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30",
                "16:00", "16:30", "17:00", "17:30", "18:00"]
            return Response(horas)
