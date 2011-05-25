from PIL import Image, ImageDraw, ImageColor

from templeton.draw.core import BaseIllustrator

class ShieldIllustrator(BaseIllustrator):
    def illustrate(self, shield_design):
        image = Image.open("/home/ross/projects/coa/templeton/trunk/target/templeton-0.0.1/templeton/resources/template.png")
        
        c1 = ImageColor.getrgb('#%s' % shield_design['colour1_hex'])
        c2 = ImageColor.getrgb('#%s' % shield_design['colour2_hex'])
        
        ImageDraw.floodfill(image, (5, 5), c1)
        ImageDraw.floodfill(image, (295, 5), c2)
        return image

