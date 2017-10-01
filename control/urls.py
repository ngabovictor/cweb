from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from control.models import mailbox, order
from control import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login, name= 'login'),
    url(r'^auth', views.auth_view, name = 'Auth'),
    url(r'^control', views.control, name = 'Control'),
    url(r'^invalid', views.invalid_login, name = 'invalid'),
    url(r'^mailbox', views.messages, name= 'messages'),
    url(r'^orders', views.orders, name= 'orders'),
    url(r'^login', views.login, name= 'login'),
    url(r'^logout', views.logout, name= 'login'),
    url(r'^message/0(?P<message_id>\d+)', views.message_view, name= 'message_view'),
    url(r'^order/0(?P<order_id>\d+)', views.order_view, name= 'order_view'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)