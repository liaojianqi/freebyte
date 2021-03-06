from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from freebyte.activities.models import Notification
from freebyte.decorators import ajax_required


@login_required
def notifications(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user)
    unread = Notification.objects.filter(to_user=user, is_read=False)
    for notification in unread:
        notification.is_read = True  # pragma: no cover
        notification.save()  # pragma: no cover

    return render(request, 'activities/notifications.html',
                  {'notifications': notifications})


@login_required
@ajax_required
def last_notifications(request):
    user = request.user
    notifications = Notification.call_latest_notifications(user)
    return render(request,
                  'activities/last_notifications.html',
                  {'notifications': notifications})


## TO DO
## DEPRECATED
@login_required
@ajax_required
def check_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(to_user=user,
                                                is_read=False)[:5]
    return HttpResponse(len(notifications))
