# -*- coding: utf-8 -*-
import json

import requests
from requests import exceptions

from sms_wrapper.sms_wrapper.models import Log
from sms_wrapper import excepts


class HandlerLog(object):
    def save_log(self, data, output):
        pass


class HandlerLogDB(HandlerLog):
    def save_log(self, data, output):
        data = json.dumps(data)
        output = json.dumps(output)
        Log(data=data, output=output).save()


class BaseHandler(object):

    url = None
    name = None

    def get_data_api(self, data):
        try:
            return requests.get(self.url, params=data)
        except (exceptions.ConnectionError, exceptions.ConnectTimeout, exceptions.HTTPError, TypeError, ):
            raise excepts.ConnectionErrorApiException('error connect api %s ' % self.name_class)

    @property
    def name_class(self):
        return self.name or self.__class__.__name__

    def send(self, user_data):
        if self.url is None:
            raise excepts.NotUrlApiException('not url api %s' % self.name_class)
        response = self.get_data_api(user_data)

        if not response.ok:
            raise excepts.NotUrlApiException('invalid response %s' % self.name_class)

        data = response.json()

        if hasattr(self, 'save_log'):
            self.save_log(user_data, data)

        return data
