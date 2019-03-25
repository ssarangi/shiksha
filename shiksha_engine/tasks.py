from __future__ import absolute_import

from celery import Celery
from celery.schedules import crontab

import os
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('tasks',
             broker='amqp://admin:mypass@rabbit:5672/',
             backend='amqp://admin:mypass@rabbit:5672/',
             include=['tasks'])


@app.task
def problem_generation_task():
    print("Hello Worlddddddddddd")


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    print("Setting up periodic tasks")
    # Calls test('world') every 10 seconds
    sender.add_periodic_task(10.0, problem_generation_task.s(), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     test.s('Happy Mondays!'),
    # )
