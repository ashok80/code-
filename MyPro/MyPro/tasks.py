# Create your tasks here
from __future__ import absolute_import, unicode_literals

from App.models import UserProfile
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from background_task import background
from background_task.tasks import Task


@background()
def unexpire():
    UserProfile.objects.filter(is_suspended=True).update(is_suspended=False)


@background()
def suspend():
    now = datetime.datetime.now() + timezone.timedelta(days=91)
    inactive_users = User.objects.filter(last_login__lt=now)
    for user in inactive_users:
        UserProfile.objects.filter(user=user).update(is_suspended=True)

unexpire(repeat=Task.EVERY_4_WEEKS)
suspend(repeat=Task.EVERY_4_WEEKS)
