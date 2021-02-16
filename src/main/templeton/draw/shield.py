"""
Classes for drawing the shield component of a coat of arms.
"""
from PIL import ImageColor, ImageDraw
from templeton.draw.core import BaseIllustrator


class ShieldIllustrator(BaseIllustrator):
    """
    Defines how to draw the shield.
    """

    def illustrate(self, shield_design, image):
        """
        Draws a shield by taking the colours in the design and applying them
        to two halves of an image.
        """

        fur = ImageColor.getrgb("#%s" % shield_design["fur"]["hex"])
        tincture = ImageColor.getrgb("#%s" % shield_design["tincture"]["hex"])

        ImageDraw.floodfill(image, (116, 67), fur)
        ImageDraw.floodfill(image, (253, 77), tincture)
        ImageDraw.floodfill(image, (144, 201), tincture)
        ImageDraw.floodfill(image, (214, 198), fur)

        return image
