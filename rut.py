import sys

sys.path.append('/home/ross/workspace/elk/src/main/')

import elk
from elk import core
from elk import python

params = dict(
              name="templeton", 
              version="0.0.1", 
              url="http://rossfenning.co.uk/", 
              author="Ross Fenning", 
              author_email="ross.fenning@gmail.com", 
    )

if __name__ == "__main__":
    elk.main(params)
