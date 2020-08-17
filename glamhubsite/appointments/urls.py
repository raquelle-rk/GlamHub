from django.urls import path

from . import views

app_name = 'appointments'
urlpatterns = [
    path('<str:slug>/create/', views.AppointmentCreateView.as_view(), name='create'), # noqa
    path('<str:slug>/list/', views.list_appointments, name='list'), # noqa
    path('<int:pk>/approve/', views.approve_appointment, name='approve'), # noqa
    path('<int:pk>/reject/', views.reject_appointment, name='reject'), # noqa




]
