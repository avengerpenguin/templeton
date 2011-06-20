"""
Contains class for illustrating the overall coat of arms.
"""
from PIL import Image

from templeton.draw.core import BaseIllustrator
from templeton.draw.shield import ShieldIllustrator
from templeton.draw.motto import MottoIllustrator

class CoatOfArmsIllustrator(BaseIllustrator):
    """
    Defines how to illustrate the overall coat of arms, mostly by handing
    down to sibling classes and arranging images generated therein.
    """
    def illustrate(self, coa_design, template_image):
        """
        Hands over to a ShieldIllustrator to generate a 300x300 shield image
        and places it centred within a 500x500 white box.
        """
        image = Image.new('RGBA', (380, 373), (0, 0, 0, 0))
        shield = ShieldIllustrator().illustrate(coa_design['shield'],
                                                template_image)
        image.paste(shield, (0, 0, 380, 373))

        motto_template = Image.new('RGBA', (350, 50), (0, 0, 0, 0))
        motto = MottoIllustrator().illustrate(
                                              coa_design['motto'],
                                              motto_template
                                              )

        motto_offset = (image.size[0] - motto.size[0]) / 2
        _, _, _, mask = motto.convert('RGBA').split()
        image.paste(motto, (motto_offset, 255), mask=mask)

        return image
