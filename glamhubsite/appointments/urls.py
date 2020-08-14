from django.urls import path

from . import views

app_name = 'appointments'
urlpatterns = [
    path('<uuid:pk>/create/', views.AppointmentCreateView.as_view(), name='create'), # noqa
]
