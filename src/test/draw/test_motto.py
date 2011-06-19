import unittest

from templeton.draw.motto import MottoIllustrator

class MottoIllustratorTest(unittest.TestCase):
    def setUp(self):
        pass

    def testIllustrate(self):
        motto_illutrator = MottoIllustrator()
        motto_image = motto_illutrator.illustrate('Spem Successus Alit', None)
        
        motto_image.save(open('/tmp/motto.png', 'w'))
