# -*- coding: utf-8 -*-
from sms_wrapper.sms_wrapper import excepts


def get_handler(handler_name):
    try:
        handler = __import__('sms_wrapper.handler', fromlist=(handler_name, ))
        return handler.__dict__[handler_name]()
    except KeyError:
        raise excepts.LoadHandlerException('not handler %s' % handler_name)
