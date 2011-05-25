class BaseIllustrator(object):
    def illustrate(self, design):
        raise NotImplementedError(
            "This illustrator doesn't know how to draw anything."
            )
