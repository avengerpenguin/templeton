"""
Classes for building a complete coat of arms.
"""

from templeton.design.core import BaseDesigner
from templeton.design.shield import ShieldDesigner

class CoatOfArmsDesigner(BaseDesigner):
    """
    Designs a complete coat of arms, msotly by handing off to sibling
    classes to build each component.
    """
    def __init__(self):
        self.shield_designer = ShieldDesigner()
        super(CoatOfArmsDesigner, self).__init__() 

    def design(self, profile):
        coa = dict()
        coa['shield'] = self.shield_designer.design(profile)
        return coa
