import unittest

from templeton.extract.core import BaseExtractor, ConfigNotSetError

class BaseExtractorTest(unittest.TestCase):

    def setUp(self):
        self.extractor = BaseExtractor()
        self.valid_config_key = 'valid config key'
        self.valid_config_value = 'valid config value'
        self.invalid_config_key = 'valid config key'

    def testSetAndGetConfig(self):
        self.extractor.set_config(self.valid_config_key, self.valid_config_value)
        self.assertEquals(
            self.valid_config_value,
            self.extractor.get_config(self.valid_config_key)
            )

    def testGetConfigThrowsErrorWhenConfigNotSet(self):
        try:
            self.extractor.get_config(self.invalid_config_key)
        except ConfigNotSetError, e:
            self.assertEquals(u'Config not set: %s' % self.invalid_config_key, str(e))
        else:
            fail('Expected a config error when fetching invalid key.')

    def testExtractThrowsNotImplementedError(self):
        self.assertRaises(NotImplementedError, self.extractor.extract)
