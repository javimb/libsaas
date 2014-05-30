from libsaas.services import base
from libsaas import http, parsers


class ApplicationBase(base.RESTResource):

    path = 'application'

    def create(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()


class Applications(ApplicationBase):

    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    @base.apimethod
    def filter(self, **kwargs):
        """
        Get a collection of applications that match with the params.
        """
        request = http.Request('GET', self.get_url(), kwargs)
        return request, parsers.parse_json


class Application(ApplicationBase):

    @base.apimethod
    def timeline(self, **kwargs):
        """
        Get the application's timeline
        """
        request = http.Request('GET', '{0}/{1}'.format(self.get_url(),
            'timeline'), kwargs)
        return request, parsers.parse_json