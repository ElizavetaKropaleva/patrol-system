from django.db import models


class Test(models.Model):
    test = models.CharField()


class OsData(models.Model):
    OS = models.CharField()
    description = models.CharField()
    release = models.CharField()
    codename = models.CharField()
    architecture = models.CharField()
    kernel = models.CharField()
    type = models.CharField()


class CpuData(models.Model):
    modes = models.CharField()
    vendor = models.CharField()
    model = models.CharField()
    CPUs = models.CharField()
    threads = models.CharField()
    cores_per_socket = models.CharField()
    sockets = models.CharField()


class Logs(models.Model):
    date = models.DateField()
    time = models.TimeField()
    function = models.CharField()
    event = models.CharField()