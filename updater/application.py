#!/usr/bin/env python

from celery import Celery

app = Celery('updater',
             broker='redis://localhost:6379/0',
             include=['updater.tasks'])

# CELERY CONFIGURATION
app.conf.update(
    result_expires=3600
)

if __name__ == '__main__':
    app.start()
