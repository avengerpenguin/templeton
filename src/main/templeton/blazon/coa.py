"""
Classes relating to blazoning a Coat of Arms at the top level. Generally, code
here will be passing down to the Blazoners for each constituent part.
"""
from templeton.blazon.shield import ShieldBlazoner


class CoatOfArmsBlazoner:
    """
    Class for blazoning a complete Coat of Arms. Constituent parts hand down to
    other classes for those parts.
    """

    blazon = lambda coa_design: "%s" % (ShieldBlazoner().blazon(coa_design["shield"]))
