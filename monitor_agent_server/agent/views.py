from django.shortcuts import render
from django.http import HttpResponse
from .monitor import collect, serialize, log


def fetch(request):
    text = collect()
    text = serialize(text)
    log('send state to %s' % get_client_ip(request))
    return HttpResponse(text)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
