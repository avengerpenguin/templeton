"""
Classes specifically related to blazoning just the shield component.
"""


class ShieldBlazoner:
    """
    Blazons (describes) a shield based on a given design for the shield part.
    """

    blazon = lambda shield_design: "Per {} {} and {}".format(
        shield_design["ordinary"],
        shield_design["fur_name"],
        shield_design["tincture_name"],
    )
