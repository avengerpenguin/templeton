import unittest

from templeton.design.coa import CoatOfArmsDesigner
from templeton.draw.coa import CoatOfArmsIllustrator

from PIL import Image

class CoatOfArmsIllustratorTest(unittest.TestCase):
    def setUp(self):
        pass

    def testIllustrate(self):
        profile = {'family_name': 'Fenning'}
        designer = CoatOfArmsDesigner()
        design = designer.design(profile)
        coai = CoatOfArmsIllustrator()
        template_image = Image.open("test/resources/template.png")
        image = coai.illustrate(design, template_image)
        image.save(open('/tmp/out.png', 'w'))
