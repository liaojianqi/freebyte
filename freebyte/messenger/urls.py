from django.conf.urls import url

from freebyte.messenger import views

urlpatterns = [
    url(r'^$', views.inbox, name='inbox'),
    url(r'^send/$', views.send, name='send_message'),
    url(r'^check/$', views.check, name='check_message'),
    url(r'^delete/$', views.delete, name='delete_message'),
    url(r'^receive/$', views.receive, name='receive_message'),
    url(r'^(?P<username>[^/]+)/$', views.messages, name='messages'),
]
