# -*- coding: utf-8 -*-

from MyPro.celery import app as celery_app
import threading

__all__ = ('celery_app',)

def file_main():
    print("running celery app")
    celery_app.start(['celery', '-A', 'MyPro', 'beat'])

# x = threading.Thread(target=file_main, daemon=True)
# x.start()
