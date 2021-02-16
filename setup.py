#!/usr/bin/env python

from distutils.core import setup

setup(
    name="Templeton",
    packages=[
        "templeton",
        "templeton.design",
        "templeton.extract",
        "templeton.draw",
        "templeton.resources",
    ],
    version="0.1",
    url="http://rossfenning.co.uk/",
    author="Ross Fenning",
    author_email="ross.fenning@gmail.com",
    package_dir={"": "src/main"},
)
