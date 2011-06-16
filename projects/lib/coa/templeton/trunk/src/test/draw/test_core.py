import unittest

from templeton.draw.core import BaseIllustrator

class BaseIllustratorTest(unittest.TestCase):
    def testIllustrateThrowsNotImplementedError(self):
        illustrator = BaseIllustrator()
        self.assertRaises(NotImplementedError, illustrator.illustrate, dict(), None)
