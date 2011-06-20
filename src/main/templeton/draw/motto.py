"""
Classes for drawing a motto section under the shield.
"""
import sys, uuid, os, subprocess

from PIL import Image, ImageColor, ImageDraw, ImageFont

from templeton.draw.core import BaseIllustrator

class MottoIllustrator(BaseIllustrator):
    """
    Motto illustrator writes the given text in a fixed box and arcs it.
    """
    def illustrate(self, motto, motto_image):
        motto_image = Image.new(
                                   'RGBA', (350, 50),
                                   (0,0,0,0)
                                   )

        motto_draw = ImageDraw.Draw(motto_image)

        image_width = motto_image.size[0]

        font = ImageFont.truetype(
            '/usr/share/fonts/truetype/ttf-georgewilliams/CUPOU___.TTF', 24)
        text_colour = ImageColor.getrgb('#000000')

        text_size = motto_draw.textsize(motto, font=font)
        text_x_offset = (image_width / 2) - (text_size[0] / 2)

        uid = str(uuid.uuid4())
        pre_filename = os.path.join('/', 'tmp', '%s-pre.png' % uid)
        post_filename = os.path.join('/', 'tmp', '%s-post.png' % uid)

        motto_draw.text((text_x_offset, 10), motto, fill=text_colour, font=font)
        #motto_image = motto_image.convert('RGBA')
        motto_image.save(pre_filename, 'PNG')

        curver = subprocess.Popen(
                                  [
                                   'convert', pre_filename, '-virtual-pixel',
                                   'transparent', '-rotate', '180', '-distort',
                                   'Arc', '140', '-rotate', '180',
                                   post_filename
                                   ]
                                  )
        curver.wait()

        curved_image = Image.open(post_filename)
        #curved_image = curved_image.convert('RGBA')

        os.remove(pre_filename)
        os.remove(post_filename)

        return curved_image
