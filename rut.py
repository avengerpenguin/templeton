import sys

import elk
from elk import core, python

params = dict(
              name="templeton",
              version="0.2.2",
              url="http://rossfenning.co.uk/",
              author="Ross Fenning",
              author_email="ross.fenning@gmail.com",
              packages=['templeton', 'templeton.design', 'templeton.extract',
                        'templeton.draw', 'templeton.util'],
              depends=['python-mock', 'python-unit', 'python-imaging',
                       'imagemagick', 'ttf-georgewilliams']
    )

if __name__ == "__main__":
    elk.main(params)
