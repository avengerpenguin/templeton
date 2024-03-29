import elk

params = dict(
    name="templeton",
    version="0.3.1",
    url="http://rossfenning.co.uk/",
    author="Ross Fenning",
    author_email="ross.fenning@gmail.com",
    packages=[
        "templeton",
        "templeton.design",
        "templeton.extract",
        "templeton.draw",
        "templeton.util",
    ],
    depends=[
        "python-mock",
        "python-unit",
        "python-imaging",
        "imagemagick",
        "ttf-georgewilliams",
        "lorem-ipsum-generator",
    ],
)

if __name__ == "__main__":
    elk.main(params)
