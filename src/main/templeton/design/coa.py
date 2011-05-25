from templeton.design.core import BaseDesigner
from templeton.design.shield import ShieldDesigner

class CoatOfArmsDesigner(BaseDesigner):

    def __init__(self):
        self.shield_designer = ShieldDesigner()
        super(CoatOfArmsDesigner, self).__init__() 

    def design(self, profile):
        coa = dict()
        coa['shield'] = self.shield_designer.design(profile)
        return coa
