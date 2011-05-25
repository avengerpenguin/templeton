import os, unittest, random

from templeton.design.shield import ShieldDesigner

class ShieldDesignerTest(unittest.TestCase):
    def setUp(self):
        self.designer = ShieldDesigner()
        self.family_name = "Some Family Name"
        self.profile = dict(family_name=self.family_name)

    def testPickColourReturnsTwoColours(self):
        seed = os.urandom(random.randint(1, 256))
        colours = self.designer.pick_colours(seed)

        self.assertEquals(2, len(colours))

        colour1, colour2 = colours
        self.assertEquals(2, len(colour1))
        self.assertEquals(2, len(colour2))

        assert colour1 in self.designer.colourlist
        assert colour2 in self.designer.colourlist

        colour1_hex, colour1_name = colour1
        colour2_hex, colour2_name = colour2

    def testProfileWithSurnameMakesDesignReturnShieldWithTwoColours(self):
        design = self.designer.design(self.profile)
        assert design.has_key('colour1_hex')
        assert design.has_key('colour1_name')
        assert design.has_key('colour2_hex')
        assert design.has_key('colour2_name')
