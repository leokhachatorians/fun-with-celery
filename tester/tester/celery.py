from __future__ import absolute_import
import os
from django.conf import settings
from celery import Celery
from celery.signals import worker_process_init
from multiprocessing import current_process

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tester.settings')

app = Celery('tester')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@worker_process_init.connect
def fix_multiprocessing(**kwargs):
    try:
        current_process()._config
    except AttributeError:
        current_process()._config = {'semprefix': '/mp'}

@app.task(bind=True)
def debug_task(self):
    print("Celery Works")
