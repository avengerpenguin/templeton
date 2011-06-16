import sys

import elk
from elk import core, python

params = dict(
              name="templeton", 
              version="0.0.5", 
              url="http://rossfenning.co.uk/", 
              author="Ross Fenning", 
              author_email="ross.fenning@gmail.com",
              packages=['templeton', 'templeton.design', 'templeton.extract',
                        'templeton.draw', 'templeton.resources', 'templeton.util'],
              depends=['python-mock', 'python-unit', 'python-imaging']
    )

if __name__ == "__main__":
    elk.main(params)
