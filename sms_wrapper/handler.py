# -*- coding: utf-8 -*-
from sms_wrapper.sms_wrapper.base_handler import BaseHandler, HandlerLogDB


class Smsc(BaseHandler, HandlerLogDB):
    url = 'http://smsc.ru/some­api/message/'
    name = 'sms­центр'


class SmsTraffic(BaseHandler, HandlerLogDB):
    url = 'http://smstraffic.ru/super­api/message/'
    name = 'sms­траффик'
