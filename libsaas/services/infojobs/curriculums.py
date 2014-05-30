from libsaas.services import base
from libsaas import http, parsers


class CurriculumBase(base.RESTResource):

    path = 'curriculum'

    def create(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def update(self, *args, **kwargs):
        raise base.MethodNotSupported()

    def delete(self, *args, **kwargs):
        raise base.MethodNotSupported()


class Curriculums(CurriculumBase):
    pass


class Curriculum(CurriculumBase):

    @base.apimethod
    def cvtext(self):
        """
        Get the curriculum's text
        """
        request = http.Request('GET', '{0}/{1}'.format(self.get_url(),
            'cvtext'))
        return request, parsers.parse_json

    @base.apimethod
    def education(self):
        """
        Get the curriculum's education
        """
        request = http.Request('GET', '{0}/{1}'.format(self.get_url(),
            'education'))
        return request, parsers.parse_json

    @base.apimethod
    def experience(self):
        """
        Get the curriculum's experience
        """
        request = http.Request('GET', '{0}/{1}'.format(self.get_url(),
            'experience'))
        return request, parsers.parse_json

    @base.apimethod
    def futurejob(self):
        """
        Get the curriculum's futurejob
        """
        request = http.Request('GET', '{0}/{1}'.format(self.get_url(),
            'futurejob'))
        return request, parsers.parse_json

    @base.apimethod
    def personaldata(self):
        """
        Get the curriculum's personaldata
        """
        request = http.Request('GET', '{0}/{1}'.format(self.get_url(),
            'personaldata'))
        return request, parsers.parse_json

    @base.apimethod
    def skill(self):
        """
        Get the curriculum's skill
        """
        request = http.Request('GET', '{0}/{1}'.format(self.get_url(),
            'skill'))
        return request, parsers.parse_json
