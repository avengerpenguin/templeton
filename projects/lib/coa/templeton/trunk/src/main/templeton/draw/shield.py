"""
Classes for drawing the shield component of a coat of arms.
"""
from PIL import Image, ImageDraw, ImageColor

from templeton.draw.core import BaseIllustrator

class ShieldIllustrator(BaseIllustrator):
    """
    Defines how to draw the shield.
    """
    def illustrate(self, shield_design):
        """
        Draws a shield by taking the colours in the design and applying them
        to two halves of an image.
        """
        image = Image.open("templeton/resources/template.png")
        
        colour1 = ImageColor.getrgb('#%s' % shield_design['colour1_hex'])
        colour2 = ImageColor.getrgb('#%s' % shield_design['colour2_hex'])
        
        ImageDraw.floodfill(image, (5, 5), colour1)
        ImageDraw.floodfill(image, (295, 5), colour2)
        return image

