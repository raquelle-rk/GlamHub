from datetime import timedelta

from django.core.mail import send_mail
from django.utils import timezone
from django.template.loader import render_to_string

from celery.decorators import periodic_task
# from celery.schedules import crontab
from celery.utils.log import get_task_logger

from appointments.models import Appointment

LOGGER = get_task_logger(__name__)


def send_email(appointment):
    """Send reminder"""
    subject = 'Appointment Remider'
    message = None
    from_email = 'glamhubsite.com'
    html_message = render_to_string(
        'feedback/appointment_reminder_email.html',
        context={
            'client': appointment.client.username,
            'business_name': appointment.portfolio.business_name,
            'description': appointment.description,
            'appointment_date': appointment.appointment_date
        }
    )
    try:
        send_mail(
            subject, message, from_email,
            [appointment.client.email, appointment.artist.email],
            html_message=html_message)
    except Exception:
        msg = "Failed to send email to: {}"
        LOGGER.info(msg.format(appointment.client.username))


@periodic_task(
    # run_every=crontab(minute=0, hour=5),
    run_every=timedelta(seconds=30),
    name=__name__ + '.send_appointment_reminder', ignore_result=True)
def send_appointment_reminder():
    # Do stuff
    LOGGER.info("start sending out emails")
    today = timezone.now().date()
    appointments = Appointment.objects.filter(
        is_approved=True,
        appointment_date=today)
    for appointment in appointments:
        send_email(appointment)
    LOGGER.info("finished sending out emails")
