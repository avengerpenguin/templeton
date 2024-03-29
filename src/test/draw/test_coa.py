import unittest

from PIL import Image
from templeton.design.coa import CoatOfArmsDesigner
from templeton.draw.coa import CoatOfArmsIllustrator


class CoatOfArmsIllustratorTest(unittest.TestCase):
    def setUp(self):
        pass

    def testIllustrate(self):
        profile = {"family_name": "Fenning"}
        designer = CoatOfArmsDesigner()
        design = designer.design(profile)
        coai = CoatOfArmsIllustrator()
        template_image = Image.open(
            "test/resources/shield_and_motto_template.png"
        )
        image = coai.illustrate(design, template_image)
        image.save(open("/tmp/out.png", "w"))
