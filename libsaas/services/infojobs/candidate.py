from libsaas.services import base
from libsaas import http, parsers


class Candidate(base.RESTResource):

    path = 'candidate'

    def create(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()

    @base.apimethod
    def skill(self, category_id):
        """
        Get all the candidate skills available for a given skill category
        """
        request = http.Request('GET', '{0}/{1}'.format(self.get_url(),
            'skill'), category_id)
        return request, parsers.parse_json

    @base.apimethod
    def skillcategory(self):
        """
        Get all the available skill categories
        """
        request = http.Request('GET', '{0}/{1}'.format(self.get_url(),
            'skillcategory'))
        return request, parsers.parse_json