import unittest
import json

from libsaas.executors import test_executor
from libsaas.services import infojobs


class InfojobsTestCase(unittest.TestCase):

    def setUp(self):
        self.executor = test_executor.use()
        self.executor.set_response(b'{}', 200, {})

        self.service = infojobs.Infojobs('client_id', 'client_secret')

    def serialize(self, data):
        return json.dumps(data)

    def expect(self, uri, method=None, params=None):
        self.assertEqual(self.executor.request.uri,
            'https://api.infojobs.net/api/1/{0}'.format(uri))
        if method:
            self.assertEqual(method, self.executor.request.method)
        if params:
            self.assertEqual(self.executor.request.params, params)

    def test_offer(self):
        self.service.offers().get()
        self.expect('offer', 'GET')

        params = {'province': 'Almeria'}
        self.service.offers().filter(**params)
        self.expect('offer', 'GET', params)

        self.service.offer('offer_id').get()
        self.expect('offer/offer_id', 'GET')

        self.service.offer('offer_id').killerquestion()
        self.expect('offer/offer_id/killerquestion', 'GET')

        self.service.offer('offer_id').openquestion()
        self.expect('offer/offer_id/openquestion', 'GET')

        self.service.offer('offer_id').question()
        self.expect('offer/offer_id/question', 'GET')

        params = {'offerID': 'offer_id', 'offerKillerQuestions': ['foo'],
            'offerOpenQuestions': ['bar']}
        self.service.offer('offer_id').create_application(**params)
        self.expect('offer/offer_id/application', 'POST', params)

    def test_application(self):
        self.service.applications().get()
        self.expect('application', 'GET')

        params = {'hideRejected': 'true'}
        self.service.applications().filter(**params)
        self.expect('application', 'GET', params)

        self.service.application('application_id').get()
        self.expect('application/application_id', 'GET')

        data = {'hide': 'true'}
        self.service.application('application_id').update(self.serialize(data))
        self.expect('application/application_id', 'PUT', self.serialize(data))

        params = {'page': 2}
        self.service.application('application_id').timeline(**params)
        self.expect('application/application_id/timeline', 'GET', params)

    def test_coverletters(self):
        self.service.coverletters().get()
        self.expect('coverletter', 'GET')

    def test_curriculums(self):
        self.service.curriculums().get()
        self.expect('curriculum', 'GET')

        self.service.curriculum('cvcode').get()
        self.expect('curriculum/cvcode', 'GET')

        self.service.curriculum('cvcode').cvtext()
        self.expect('curriculum/cvcode/cvtext', 'GET')

        self.service.curriculum('cvcode').education()
        self.expect('curriculum/cvcode/education', 'GET')

        self.service.curriculum('cvcode').experience()
        self.expect('curriculum/cvcode/experience', 'GET')

        self.service.curriculum('cvcode').futurejob()
        self.expect('curriculum/cvcode/futurejob', 'GET')

        self.service.curriculum('cvcode').personaldata()
        self.expect('curriculum/cvcode/personaldata', 'GET')

        self.service.curriculum('cvcode').skill()
        self.expect('curriculum/cvcode/skill', 'GET')

    def test_candidate(self):
        self.service.candidate().get()
        self.expect('candidate', 'GET')

        self.service.candidate().skill('category_id')
        self.expect('candidate/skill', 'GET')

        self.service.candidate().skillcategory()
        self.expect('candidate/skillcategory', 'GET')
