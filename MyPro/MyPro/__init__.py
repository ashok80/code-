# -*- coding: utf-8 -*-

from MyPro.celery import app as celery_app
import threading

__all__ = ('celery_app',)

def run_worker():
    """
    Method used to run the worker thread.
    """
    print("running celery worker")
    celery_app.start(['celery', '-A', 'MyPro', 'worker', '-l', 'debug'])

def run_beat():
    """
    method used to run the beat thread
    """
    print("running celery beat")
    celery_app.start(['celery', '-A', 'MyPro', 'beat', '-l', 'debug'])

worker_thread = threading.Thread(target=run_worker, daemon=True)
beat_thread = threading.Thread(target=run_beat, daemon=True)

worker_thread.start()
beat_thread.start()
