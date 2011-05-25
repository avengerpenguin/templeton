"""
Base classes for designing components of a coat of arms.
"""
class BaseDesigner(object):
    """
    Overall parent class for any designer that ensures design() is implemented.
    """
    def design(self, profile):
        """
        Designs any part of a coat of arms as defined in the implementing child
        class. Takes a dict representation of someone's profile and should return
        another dict that defines visual aspects of the component.
        """
        raise NotImplementedError(
            "This designer doesn't know how to design anything yet."
            )
