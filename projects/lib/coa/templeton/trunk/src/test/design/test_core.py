import unittest

from templeton.design.core import BaseDesigner

class BaseDesignerTest(unittest.TestCase):
    def testDesignThrowsNotImplementedError(self):
        designer = BaseDesigner()
        self.assertRaises(NotImplementedError, designer.design, dict())
