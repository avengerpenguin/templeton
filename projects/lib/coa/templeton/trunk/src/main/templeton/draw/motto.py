import tempfile, sys, uuid, os
import subprocess, base64

from PIL import Image, ImageColor, ImageDraw, ImageFont

from templeton.draw.core import BaseIllustrator

class MottoIllustrator(BaseIllustrator):
    def illustrate(self, motto, image):
        motto_image = Image.new('RGB', (400, 50), ImageColor.getrgb('#EEEEEE'))
        motto_draw = ImageDraw.Draw(motto_image)

        image_size = motto_image.size
        image_height = motto_image.size[1]
        image_width = motto_image.size[0]

        font = ImageFont.truetype('/usr/share/fonts/truetype/ttf-georgewilliams/CUPOU___.TTF', 24)
        text_colour = ImageColor.getrgb('#000000')

        text_size = motto_draw.textsize(motto, font=font)
        x = (image_width / 2) - (text_size[0] / 2)

        uid = str(uuid.uuid4())
        pre_filename = os.path.join('/', 'tmp', '%s-pre.png' % uid)
        post_filename = os.path.join('/', 'tmp', '%s-post.png' % uid)

        motto_draw.text((x, 10), motto, fill=text_colour, font=font)
        motto_image.save(pre_filename, 'PNG')

        curver = subprocess.Popen(['convert', pre_filename, '-virtual-pixel', 'White', '-distort', 'Arc', '60', post_filename], stderr=sys.stderr)
        curver.wait()

        curved_image = Image.open(post_filename)

        return curved_image
