# -*- coding: utf-8 -*-
from django.test import TestCase

from sms_wrapper import get_handler
from sms_wrapper import excepts, base_handler


class HandlerDummy(base_handler.BaseHandler):
    pass


class Handler(base_handler.BaseHandler):
    url = ''

    class Response(object):
            ok = True
            def json(self):
                return {'status': 'ok', 'phone': '79852756363'}

    class ResponseError(object):
            ok = True
            def json(self):
                return {'status': 'error', 'phone': '79852756363', 'error_code': -3500, 'error_msg': 'text'}

    def get_data_api(self, data):
        return self.Response()


class SmsHandlerTestCase(TestCase):
    def test_factory_handler(self):
        try:
            get_handler('asd')
        except excepts.LoadHandlerException as e:
            self.assertTupleEqual(e.args, ('not handler asd', ))
        self.assertTrue(isinstance(get_handler('Smsc'), base_handler.BaseHandler))

    def test_handler_dummy(self):
        try:
            sms = HandlerDummy()
            sms.send({'phone': '79852756363', 'text': 'asdasdasdas'})
        except excepts.NotUrlApiException as e:
            self.assertTupleEqual(e.args, ('not url api HandlerDummy', ))

    def test_handler(self):
        sms = Handler()
        self.assertDictEqual(
            sms.send({'phone': '79852756363', 'text': 'asdasdasdas'}),
            {'status': 'ok', 'phone': '79852756363'}
        )
        Handler.get_data_api = (lambda self, data: self.ResponseError())
        sms = Handler()
        self.assertDictEqual(
            sms.send({'phone': '79852756363', 'text': 'asdasdasdas'}),
            {'status': 'error', 'phone': '79852756363', 'error_code': -3500, 'error_msg': 'text'}
        )