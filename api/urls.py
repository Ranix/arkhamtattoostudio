from django.urls import path

from api import views

urlpatterns = [
    # path('eventlist/', views.EventList.as_view()),
    # path('dayevents/<slug:date>/', views.EventDate.as_view()),
    path('freehours/<slug:date>/', views.FreeHours.as_view())
]
