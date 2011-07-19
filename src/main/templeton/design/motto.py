"""
Classes for designing a motto portion of a Coat of Arms.
"""

from templeton.design.core import BaseDesigner

import random, lipsum

class MottoDesigner(BaseDesigner):
    """
    Designs the text of a motto. Currently uses the family name of the profile.
    """
    def design(self, profile):
        if profile.has_key('family_name'):
            family_name = profile['family_name']

            random.seed(family_name)
            lipsum_generator = lipsum.Generator()
            lipsum_generator.sentence_mean = 3
            lipsum_generator.sentence_sigma = 1
            
            return lipsum_generator.generate_sentence()
        else:
            return None
