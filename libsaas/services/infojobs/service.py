from libsaas.services import base
from libsaas.filters import auth

from . import offers, applications, coverletters, curriculums, candidate


class Infojobs(base.Resource):
    """
    """
    def __init__(self, client_id, client_secret, oauth_token=None):
        """
        Create a Infojobs service.

        :var client_id: Your 'Client ID' key
        :vartype client_id: str

        :var client_secret: Your 'Client scret' key.
        :vartype client_secret: str
        """
        self.apiroot = 'https://api.infojobs.net/api/1'

        self.add_filter(auth.BasicAuth(client_id, client_secret))
        if oauth_token is not None:
            self.oauth_token = oauth_token
            self.add_filter(self.add_oauth_authorization)

    def get_url(self):
        return self.apiroot

    def add_oauth_authorization(self, request):
        request.headers['Authorization'] = '{0},{1}'.format(request.headers['Authorization'],
            'OAuth {0}'.format(self.oauth_token))

    @base.resource(offers.Offer)
    def offer(self, offer_id):
        """
        Return the resource corresponding to a single offer.
        """
        return offers.Offer(self, offer_id)

    @base.resource(offers.Offers)
    def offers(self):
        """
        Return the resource corresponding to all the offers.
        """
        return offers.Offers(self)

    @base.resource(applications.Application)
    def application(self, application_id):
        """
        Return the resource corresponding to a application offer.
        """
        return applications.Application(self, application_id)

    @base.resource(applications.Applications)
    def applications(self):
        """
        Return the resource corresponding to all the applications.
        """
        return applications.Applications(self)

    @base.resource(coverletters.Coverletters)
    def coverletters(self):
        """
        Return the resource corresponding to all the coverletters.
        """
        return coverletters.Coverletters(self)

    @base.resource(curriculums.Curriculum)
    def curriculum(self, cvcode):
        """
        Return the resource corresponding to a curriculum.
        """
        return curriculums.Curriculum(self, cvcode)

    @base.resource(curriculums.Curriculums)
    def curriculums(self):
        """
        Return the resource corresponding to all the curriculums.
        """
        return curriculums.Curriculum(self)

    @base.resource(candidate.Candidate)
    def candidate(self):
        """
        Return the resource corresponding to the candidate.
        """
        return candidate.Candidate(self)
