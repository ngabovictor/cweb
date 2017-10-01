from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from control.models import mailbox, order
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone
# Create your views here.

@login_required(login_url="login")
def messages(request):

	data = {}

	data['inbox'] = mailbox.objects.all().order_by('-date');
	data['all_messages'] = mailbox.objects.all().count()
	data['unread_counter'] = mailbox.objects.filter(classifications='Unread').count()
	data['read_counter'] = mailbox.objects.filter(classifications='Read').count()
	return render(request, 'control/messages.html', data)

@login_required(login_url="login")
def orders(request):

	data = {}

	data['requests'] = order.objects.all().order_by('-classification')
	data['unread_counter'] = order.objects.filter(classification='Unread').count()
	return render(request, 'control/orders.html', data)



def login(request):
	secure = {}

	secure.update(csrf(request))
	return render(request, 'control/login.html', secure)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('control')
	else:
		return HttpResponseRedirect('invalid')

def invalid_login(request):
	return render(request, 'control/invalid.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('login')

@login_required(login_url="login")
def message_view(request, message_id):
	
	data = {}
	data['mailbox'] = mailbox.objects.all()
	data['sender'] = mailbox.objects.get(pk=message_id)
	mailbox.objects.filter(id = message_id).update(classifications='Read')
	data['unread_counter'] = mailbox.objects.filter(classifications='Unread').count()
	return render(request, 'control/message.html', data)


@login_required(login_url="login")
def order_view(request, order_id):
	
	data = {}
	data['orders'] = order.objects.all()
	data['job'] = order.objects.get(pk=order_id)
	order.objects.filter(id = order_id).update(classification='Read')
	data['unread_counter'] = order.objects.filter(classification='Unread').count()
	return render(request, 'control/order.html', data)


@login_required(login_url="login")
def control(request):

	return render(request, 'control/control.html')

