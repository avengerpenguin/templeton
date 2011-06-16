"""
Contains class for illustrating the overall coat of arms.
"""
from PIL import Image, ImageColor

from templeton.draw.core import BaseIllustrator
from templeton.draw.shield import ShieldIllustrator

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
        image = Image.new('RGB', (400, 400), ImageColor.getrgb('#FFFFFF'))
        shield = ShieldIllustrator().illustrate(coa_design['shield'],
                                                template_image)
        image.paste(shield, (50, 50, 350, 350))

        return image
