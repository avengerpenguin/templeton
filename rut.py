import sys

sys.path.append('/home/ross/workspace/elk/src/main/')

import elk
from elk import core, python

params = dict(
              name="templeton", 
              version="0.0.2", 
              url="http://rossfenning.co.uk/", 
              author="Ross Fenning", 
              author_email="ross.fenning@gmail.com",
              packages=['templeton', 'templeton.design', 'templeton.extract',
                        'templeton.draw', 'templeton.resources'],
              depends=['python-mock', 'python-unit', 'python-imaging']
    )

if __name__ == "__main__":
    print "foo"
    elk.main(params)
