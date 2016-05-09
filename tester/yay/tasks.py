from __future__ import absolute_import
from celery import shared_task
from random import randint
from celery.task import periodic_task
from celery.schedules import crontab
import pyscreenshot as ImageGrab
from datetime import datetime

@periodic_task(run_every=(crontab(minute='*/1')),
        name='screen_shotter',
        ignore_result=True)
def screen_shotter():
    time = datetime.utcnow()
    ImageGrab.grab_to_file('{}.png'.format(time))

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y
