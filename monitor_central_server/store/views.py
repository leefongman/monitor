import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models


@csrf_exempt
def upload(request):
    data = json.loads(request.POST['data'])

    info = data['cpu']
    cpu = models.CPU()
    cpu.min1 = info['1min']
    cpu.min5 = info['5min']
    cpu.min15 = info['15min']
    cpu.save()

    info = data['ram']
    ram = models.RAM()
    ram.total = info['total']
    ram.used = info['used']
    ram.free = info['free']
    ram.shared = info['shared']
    ram.buffers = info['buffers']
    ram.cached = info['cached']
    ram.save()

    info = data['hd']
    hd = models.HD()
    hd.dev = info['dev']
    hd.total = info['total']
    hd.used = info['used']
    hd.available = info['available']
    hd.percent = info['percent']
    hd.mpoint = info['mpoint']
    hd.save()

    return HttpResponse('ok')
