import unittest

from templeton.design.coa import CoatOfArmsDesigner
from templeton.draw.coa import CoatOfArmsIllustrator

class CoatOfArmsIllustratorTest(unittest.TestCase):
    def setUp(self):
        pass

    def testIllustrate(self):
        profile = {'family_name': 'Fenning'}
        designer = CoatOfArmsDesigner()
        design = designer.design(profile)
        coai = CoatOfArmsIllustrator()
        image = coai.illustrate(design)
        image.save(open('/tmp/out.png', 'w'))
