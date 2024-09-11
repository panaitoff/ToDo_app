from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from .models import Task

@shared_task
def send_task_reminders():
    tasks = Task.objects.filter(due_date__lte=timezone.now(), is_completed=False)
    for task in tasks:
        send_mail(
            f'Task "{task.title}" is due',
            f'The task "{task.title}" is due soon!',
            'from@example.com',
            [task.user.email],
            fail_silently=False,
        )
