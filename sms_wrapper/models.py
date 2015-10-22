# -*- coding: utf-8 -*-
from django.db import models


class Log(models.Model):
    data = models.TextField(verbose_name='Входящие параметры')
    output = models.TextField(verbose_name='Ответ')
    date = models.DateTimeField(auto_now_add=True)
