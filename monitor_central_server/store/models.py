from django.db import models


class CPU(models.Model):
    min1 = models.FloatField()
    min5 = models.FloatField()
    min15 = models.FloatField()
    time = models.DateTimeField(auto_now=True)


class RAM(models.Model):
    total = models.IntegerField()
    used = models.IntegerField()
    free = models.IntegerField()
    shared = models.IntegerField()
    buffers = models.IntegerField()
    cached = models.IntegerField()
    time = models.DateTimeField(auto_now=True)


class HD(models.Model):
    dev = models.CharField(max_length=256)
    total = models.IntegerField()
    used = models.IntegerField()
    available = models.IntegerField()
    percent = models.CharField(max_length=10)
    mpoint = models.CharField(max_length=256)
    time = models.DateTimeField(auto_now=True)
