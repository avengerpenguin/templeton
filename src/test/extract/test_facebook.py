import unittest
from mock import Mock

from templeton.extract.facebook import FacebookExtractor

class FacebookExtractorTest(unittest.TestCase):

    def setUp(self):
        self.extractor = FacebookExtractor()

        self.facebook_username = 'some_user_name'
        self.extractor.set_config('username', self.facebook_username)

        self.last_name = 'Some Surname'
        self.name = 'Some Name'
        self.gender = 'Some Gender'
        self.locale = 'Some Locale'

        self.fb_profile= dict(
            last_name = self.last_name,
            name = self.name,
            gender = self.gender,
            locale = self.locale
            )

    def testInitCreatesFacebookGraphApiObject(self):
        new_extractor = FacebookExtractor()
        self.assertNotEqual(None, new_extractor.api)

    def testExtractCallsGetObjectOnApiWithGivenUsername(self):
        self.extractor.api = Mock()
        self.extractor.api.get_object = Mock(return_value=dict())

        self.extractor.api.mockSetExpectation(
            'get_object',
            lambda mockobj, call, count: call.getParam(0) == self.facebook_username
            )

        self.extractor.extract()

    def testExtractReturnsDictTranslatedFromFacebookDict(self):
        self.extractor.api = Mock()
        self.extractor.api.get_object = Mock(return_value=self.fb_profile)

        self.extractor.api.mockSetExpectation(
            'get_object',
            lambda mockobj, call, count: call.getParam(0) == self.facebook_username
            )

        profile = self.extractor.extract()
        
        self.assertEquals(self.last_name, profile['family_name'])
        self.assertEquals(self.name, profile['full_name'])
        self.assertEquals(self.gender, profile['sex'])
        self.assertEquals(self.locale, profile['locale'])
