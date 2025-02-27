# your_app/tasks.py

from celery import shared_task
from django.utils.timezone import now
#from .models import TokenKey
''''
@shared_task
def delete_expired_tokens():
    expired_tokens = TokenKey.objects.filter(expires_at__lt=now()).delete()
    return f"Deleted {expired_tokens[0]} expired tokens"
'''
@shared_task
def add(x, y):
    return x + y