"""
Contains base illustrator class to define how all illustrators should work.
"""


class BaseIllustrator:
    """
    The base parent class not designed to be implemented that defines
    that all illustrators must implement the illustrate() method.
    """

    def illustrate(self, design, image):
        """
        Takes a design dict that specifies how to draw a particular component
        and then returns the image for that component. Specific implementations
        must override this in child classes.

        An image object must also be passed in on which to draw modifications.
        """
        raise NotImplementedError("This illustrator doesn't know how to draw anything.")
