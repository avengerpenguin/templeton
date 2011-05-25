from PIL import Image, ImageDraw, ImageColor

from templeton.draw.core import BaseIllustrator
from templeton.draw.shield import ShieldIllustrator

class CoatOfArmsIllustrator(BaseIllustrator):
    def illustrate(self, coa_design):
        image = Image.new('RGB', (400, 400), ImageColor.getrgb('#FFFFFF'))
        shield = ShieldIllustrator().illustrate(coa_design['shield'])
        image.paste(shield, (50, 50, 350, 350))

        return image
        
