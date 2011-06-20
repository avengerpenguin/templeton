"""
Classes for designing a motto portion of a Coat of Arms.
"""

from templeton.design.core import BaseDesigner

class MottoDesigner(BaseDesigner):
    """
    Designs the text of a motto. Currently uses the family name of the profile.
    """
    def design(self, profile):
        if profile.has_key('family_name'):
            return profile['family_name']
        else:
            return None
