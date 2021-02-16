import os
import random
import unittest

from templeton.design.shield import ShieldDesigner


class ShieldDesignerTest(unittest.TestCase):
    def setUp(self):
        self.designer = ShieldDesigner()
        self.family_name = "Some Family Name"
        self.profile = dict(family_name=self.family_name)

    def testPickColourReturnsTwoColours(self):
        seed = os.urandom(random.randint(1, 256))
        colours = self.designer.pick_colours(seed)

        assert 2 == len(colours)

        for colour in colours:
            assert colour.has_key("hex")
            assert colour.has_key("name")

            assert (colour["hex"], colour["name"]) in self.designer.colourlist

    def testPickOrdinaryReturnsAnOrdinary(self):
        seed = os.urandom(random.randint(1, 256))
        ordinary = self.designer.pick_ordinary(seed)

        assert ordinary in self.designer.ordinary_list

    def testProfileWithSurnameMakesDesignReturnShieldWithTwoColours(self):
        design = self.designer.design(self.profile)
        assert design.has_key("fur")
        assert design.has_key("tincture")
        for colour in design["fur"], design["tincture"]:
            assert colour.has_key("hex")
            assert colour.has_key("name")

    def testProfileWithSurnameMakesDesignReturnShieldWithOrdinary(self):
        design = self.designer.design(self.profile)
        assert design.has_key("ordinary")
