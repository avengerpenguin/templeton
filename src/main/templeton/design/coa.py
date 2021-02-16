"""
Classes for building a complete coat of arms.
"""

from templeton.design.core import BaseDesigner
from templeton.design.motto import MottoDesigner
from templeton.design.shield import ShieldDesigner


class CoatOfArmsDesigner(BaseDesigner):
    """
    Designs a complete coat of arms, msotly by handing off to sibling
    classes to build each component.
    """

    def __init__(self):
        self.shield_designer = ShieldDesigner()
        self.motto_designer = MottoDesigner()
        super().__init__()

    def design(self, profile):
        coa = dict()
        coa["shield"] = self.shield_designer.design(profile)
        coa["motto"] = self.motto_designer.design(profile)
        return coa
