import unittest
from unittest.mock import Mock

from templeton.design.coa import CoatOfArmsDesigner


class CoatOfArmsDesignerTest(unittest.TestCase):
    def setUp(self):
        self.profile = dict()
        self.shield = dict(some_key="some_value")

    def testDesignReturnsDictContainingShieldDesign(self):
        coa_designer = CoatOfArmsDesigner()

        shield_designer = Mock()
        shield_designer.design = Mock(return_value=self.shield)

        coa_designer.shield_designer = shield_designer

        coa = coa_designer.design(self.profile)
        self.assertEquals(self.shield, coa["shield"])
