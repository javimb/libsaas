from libsaas.services import base
from libsaas import http, parsers


class OfferBase(base.RESTResource):

    path = 'offer'

    def create(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()


class Offers(OfferBase):

    @base.apimethod
    def filter(self, **kwargs):
        """
        Get a collection of offers that match with the params.
        """
        request = http.Request('GET', self.get_url(), kwargs)
        return request, parsers.parse_json


class Offer(OfferBase):
    
    @base.apimethod
    def killerquestion(self):
        """
        Get the offer's killerquestion
        """
        request = http.Request('GET', '{0}/{1}'.format(self.get_url(),
            'killerquestion'))
        return request, parsers.parse_json

    @base.apimethod
    def openquestion(self):
        """
        Get the offer's openquestion
        """
        request = http.Request('GET', '{0}/{1}'.format(self.get_url(),
            'openquestion'))
        return request, parsers.parse_json


    @base.apimethod
    def question(self):
        """
        Get the offer's questions
        """
        request = http.Request('GET', '{0}/{1}'.format(self.get_url(),
            'question'))
        return request, parsers.parse_json

    @base.apimethod
    def create_application(self, **kwargs):
        """
        Applicate the offer.
        """
        request = http.Request('POST', '{0}/{1}'.format(self.get_url(),
            'application'), kwargs)
        return request, parsers.parse_json
