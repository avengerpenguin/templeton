"""
Provides classes for designing the shield portion of a Coat of Arms based on a
social networking profile.
"""

import hashlib

from templeton.design.core import BaseDesigner


class ShieldDesigner(BaseDesigner):
    """
    This class builds the shield part of a Coat of Arms given a profile.
    """

    colourlist = [
        ("5D8AA8", "Air Force blue"),
        ("F0F8FF", "Alice blue"),
        ("E32636", "Alizarin"),
        ("E52B50", "Amaranth"),
        ("F19CBB", "Amaranth Pink"),
        ("FFBF00", "Amber"),
        ("FF7E00", "Amber"),
        ("9966CC", "Amethyst"),
        ("FBCEB1", "Apricot"),
        ("00FFFF", "Aqua"),
        ("7FFFD4", "Aquamarine"),
        ("4B5320", "Army green"),
        ("3B444B", "Arsenic"),
        ("7BA05B", "Asparagus"),
        ("FF9966", "Atomic tangerine"),
        ("6D351A", "Auburn"),
        ("007FFF", "Azure"),
        ("F0FFFF", "Azure"),
        ("E0FFFF", "Baby blue"),
        ("F5F5DC", "Beige"),
        ("3D2B1F", "Bistre"),
        ("000000", "Black"),
        ("0000FF", "Blue"),
        ("333399", "Blue"),
        ("0247FE", "Blue"),
        ("00DDDD", "Blue-green"),
        ("8A2BE2", "violet"),
        ("79443B", "Bole"),
        ("0095B6", "Bondi blue"),
        ("0070FF", "Brandeis Blue"),
        ("B5A642", "Brass"),
        ("66FF00", "Bright green"),
        ("FF007F", "Bright pink"),
        ("08E8DE", "Bright turquoise"),
        ("FF55A3", "Brilliant rose"),
        ("FB607F", "Brink Pink"),
        ("004225", "British racing green"),
        ("CD7F32", "Bronze"),
        ("964B00", "Brown"),
        ("F0DC82", "Buff"),
        ("800020", "Burgundy"),
        ("CC5500", "Burnt orange"),
        ("E97451", "Burnt sienna"),
        ("8A3324", "Burnt umber"),
        ("702963", "Byzantium"),
        ("78866B", "Camouflage green"),
        ("592720", "Caput Mortuum"),
        ("C41E3A", "Cardinal"),
        ("960018", "Carmine"),
        ("EB4C42", "Carmine Pink"),
        ("FFA6C9", "Carnation pink"),
        ("B31B1B", "Carnelian"),
        ("99BADD", "Carolina blue"),
        ("ED9121", "Carrot orange"),
        ("ACE1AF", "Celadon"),
        ("DE3163", "Cerise"),
        ("EC3B83", "Cerise Pink"),
        ("007BA7", "Cerulean"),
        ("2A52BE", "Cerulean blue"),
        ("F7E7CE", "Champagne"),
        ("464646", "Charcoal"),
        ("DFFF00", "Chartreuse"),
        ("7FFF00", "Chartreuse"),
        ("FFB7C5", "Cherry blossom pink"),
        ("CD5C5C", "Chestnut"),
        ("7B3F00", "Chocolate"),
        ("E34234", "Cinnabar"),
        ("D2691E", "Cinnamon"),
        ("0047AB", "Cobalt"),
        ("9BDDFF", "Columbia Blue"),
        ("B87333", "Copper"),
        ("996666", "Copper rose"),
        ("FF7F50", "Coral"),
        ("F88379", "Coral pink"),
        ("FF4040", "Coral red"),
        ("893F45", "Cordovan"),
        ("FBEC5D", "Corn"),
        ("6495ED", "Cornflower blue"),
        ("FFF8E7", "Cosmic latte"),
        ("FFFDD0", "Cream"),
        ("DC143C", "Crimson"),
        ("00FFFF", "Cyan"),
        ("00B7EB", "Cyan"),
        ("00008B", "Dark Blue"),
        ("654321", "Dark Brown"),
        ("08457E", "Dark Cerulean"),
        ("986960", "Dark Chestnut"),
        ("CD5B45", "Dark Coral"),
        ("B8860B", "Dark Goldenrod"),
        ("013220", "Dark Green"),
        ("BDB76B", "Dark Khaki"),
        ("8B008B", "Dark Magenta"),
        ("03C03C", "Dark Pastel Green"),
        ("E75480", "Dark Pink"),
        ("560319", "Dark Scarlet"),
        ("E9967A", "Dark Salmon"),
        ("2F4F4F", "Dark Slate Grey"),
        ("177245", "Dark Spring Green"),
        ("918151", "Dark Tan"),
        ("00CED1", "Dark Turquoise"),
        ("9400D3", "Dark Violet"),
        ("555555", "Davy's Grey"),
        ("EF3038", "Deep Carmine Pink"),
        ("DA3287", "Deep Cerise"),
        ("B94E48", "Deep Chestnut"),
        ("C154C1", "Deep Fuchsia"),
        ("9955BB", "Deep Lilac"),
        ("CD00CC", "Deep Magenta"),
        ("FFCBA4", "Deep Peach"),
        ("FF1493", "Deep Pink"),
        ("FF9933", "Deep Saffron"),
        ("1560BD", "Denim"),
        ("EDC9AF", "Desert Sand"),
        ("1E90FF", "Dodger Blue"),
        ("00009C", "Duke Blue"),
        ("C2B280", "Ecru"),
        ("1034A6", "Egyptian Blue"),
        ("614051", "Aubergine"),
        ("7DF9FF", "Electric Blue"),
        ("00FF00", "Electric Green)"),
        ("6600FF", "Electric Indigo"),
        ("CCFF00", "Electric Lime"),
        ("BF00FF", "Electric Purple"),
        ("50C878", "Emerald"),
        ("C19A6B", "Fallow"),
        ("801818", "Falu Red"),
        ("4D5D53", "Feldgrau"),
        ("4F7942", "Fern Green"),
        ("B22222", "Firebrick"),
        ("CE2029", "Fire Engine Red"),
        ("EEDC82", "Flax"),
        ("228B22", "Forest Green"),
        ("F64A8A", "French Rose"),
        ("FF00FF", "Fuchsia"),
        ("FF77FF", "Fuchsia Pink"),
        ("E49B0F", "Gamboge"),
        ("D4AF37", "Gold"),
        ("FFD700", "Gold"),
        ("996515", "Golden brown"),
        ("FCC200", "Golden poppy"),
        ("FFDF00", "Golden yellow"),
        ("DAA520", "Goldenrod"),
        ("808080", "Grey"),
        ("465945", "Grey-asparagus"),
        ("00FF00", "Green)"),
        ("008000", "Green)"),
        ("00A550", "Green"),
        ("66B032", "Green"),
        ("ADFF2F", "Green-yellow"),
        ("5218FA", "Han Blue"),
        ("5218FA", "Han Purple"),
        ("3FFF00", "Harlequin"),
        ("DF73FF", "Heliotrope"),
        ("F400A1", "Hollywood Cerise"),
        ("FF00CC", "Hot Magenta"),
        ("FF69B4", "Hot Pink"),
        ("355E3B", "Hunter green"),
        ("138808", "India green"),
        ("00416A", "Indigo"),
        ("4B0082", "Indigo"),
        ("002FA7", "International Klein Blue"),
        ("FF4F00", "International orange"),
        ("009000", "Islamic green"),
        ("FFFFF0", "Ivory"),
        ("00A86B", "Jade"),
        ("29AB87", "Jungle green"),
        ("4CBB17", "Kelly green"),
        ("C3B091", "Khaki"),
        ("F0E68C", "Light Khaki"),
        ("CF1020", "Lava"),
        ("B57EDC", "Lavender"),
        ("E6E6FA", "Lavender"),
        ("CCCCFF", "Lavender blue"),
        ("FFF0F5", "Lavender blush"),
        ("C4C3D0", "Lavender grey"),
        ("9457EB", "Lavender indigo"),
        ("EE82EE", "Lavender magenta"),
        ("FBAED2", "Lavender pink"),
        ("967BB6", "Lavender purple"),
        ("FBA0E3", "Lavender rose"),
        ("7CFC00", "Lawn green"),
        ("FDE910", "Lemon"),
        ("FFFACD", "Lemon chiffon"),
        ("ADD8E6", "Light blue"),
        ("FFB6C1", "Light pink"),
        ("E68FAC", "Light Thulian pink"),
        ("C8A2C8", "Lilac"),
        ("BFFF00", "Lime"),
        ("00FF00", "Lime green)"),
        ("32CD32", "Lime green"),
        ("FAF0E6", "Linen"),
        ("534B4F", "Liver"),
        ("FF00FF", "Magenta"),
        ("CA1F7B", "Magenta"),
        ("FF0090", "Magenta"),
        ("AAF0D1", "Magic Mint"),
        ("F8F4FF", "Magnolia"),
        ("C04000", "Mahogany"),
        ("FBEC5D", "Maize"),
        ("6050DC", "Majorelle Blue"),
        ("0BDA51", "Malachite"),
        ("800000", "Maroon"),
        ("B03060", "Maroon"),
        ("E0B0FF", "Mauve"),
        ("915F6D", "Mauve Taupe"),
        ("73C2FB", "Maya blue"),
        ("0000CD", "Medium blue"),
        ("AF4035", "Medium carmine"),
        ("CC99CC", "Medium lavender magenta"),
        ("9370DB", "Medium purple"),
        ("00FA9A", "Medium spring green"),
        ("674C47", "Medium taupe"),
        ("191970", "Midnight Blue"),
        ("004953", "Midnight Green"),
        ("98FF98", "Mint green"),
        ("FFE4E1", "Misty rose"),
        ("ADDFAD", "Moss green"),
        ("997A8D", "Mountbatten pink"),
        ("FFDB58", "Mustard"),
        ("21421E", "Myrtle"),
        ("006633", "MSU Green"),
        ("FFDEAD", "Navajo white"),
        ("000080", "Navy Blue"),
        ("CC7722", "Ochre"),
        ("008000", "Office green"),
        ("CFB53B", "Old Gold"),
        ("FDF5E6", "Old Lace"),
        ("796878", "Old Lavender"),
        ("C08081", "Old Rose"),
        ("808000", "Olive"),
        ("6B8E23", "Olive Drab"),
        ("9AB973", "Olivine"),
        ("FF7F00", "Orange"),
        ("FB9902", "Orange"),
        ("FFA500", "Orange"),
        ("FFA000", "Orange Peel"),
        ("FF4500", "Red"),
        ("DA70D6", "Orchid"),
        ("AFEEEE", "Pale blue"),
        ("987654", "Pale brown"),
        ("AF4035", "Pale carmine"),
        ("DDADAF", "Pale chestnut"),
        ("ABCDEF", "Pale cornflower blue"),
        ("F984E5", "Pale magenta"),
        ("FADADD", "Pale pink"),
        ("DB7093", "Pale violet"),
        ("BC987E", "Pale taupe"),
        ("FFEFD5", "Papaya whip"),
        ("77DD77", "Pastel green"),
        ("FFD1DC", "Pastel pink"),
        ("40404F", "Payne's grey"),
        ("FFE5B4", "Peach"),
        ("FFCC99", "Peach-orange"),
        ("FADFAD", "Peach-yellow"),
        ("D1E231", "Pear"),
        ("CCCCFF", "Periwinkle"),
        ("1C39BB", "Persian blue"),
        ("00A693", "Persian green"),
        ("32127A", "Persian indigo"),
        ("D99058", "Persian orange"),
        ("CC3333", "Persian red"),
        ("F77FBE", "Persian pink"),
        ("FE28A2", "Persian rose"),
        ("EC5800", "Persimmon"),
        ("01796F", "Pine Green"),
        ("FFC0CB", "Pink"),
        ("FF9966", "Pink-orange"),
        ("E5E4E2", "Platinum"),
        ("CC99CC", "Plum"),
        ("FF5A36", "Portland Orange"),
        ("B0E0E6", "Powder Blue"),
        ("CC8899", "Puce"),
        ("003153", "Prussian blue"),
        ("DD00FF", "Psychedelic purple"),
        ("FF7518", "Pumpkin"),
        ("7F007F", "Purple"),
        ("A020F0", "Purple"),
        ("50404D", "Purple Taupe"),
        ("E30B5C", "Raspberry"),
        ("734A12", "Raw umber"),
        ("E3256B", "Razzmatazz"),
        ("FF0000", "Red"),
        ("ED1C24", "Red"),
        ("FE2712", "Red"),
        ("C71585", "Red-violet"),
        ("D70040", "Rich carmine"),
        ("00CCCC", "Robin egg blue"),
        ("FF007F", "Rose"),
        ("E32636", "Rose Madder"),
        ("FF66CC", "Rose pink"),
        ("AA98A9", "Rose quartz"),
        ("905D5D", "Rose Taupe"),
        ("4169E1", "Royal blue"),
        ("6B3FA0", "Royal purple"),
        ("E0115F", "Ruby"),
        ("80461B", "Russet"),
        ("B7410E", "Rust"),
        ("FF6600", "Safety orange"),
        ("F4C430", "Saffron"),
        ("FF8C69", "Salmon"),
        ("FF91A4", "Salmon pink"),
        ("F4A460", "Sandy brown"),
        ("92000A", "Sangria"),
        ("082567", "Sapphire"),
        ("FF2400", "Scarlet"),
        ("FFD800", "School bus yellow"),
        ("2E8B57", "Sea Green"),
        ("321414", "Seal brown"),
        ("FFF5EE", "Seashell"),
        ("FFBA00", "Selective yellow"),
        ("704214", "Sepia"),
        ("009E60", "Shamrock green"),
        ("FC0FC0", "Shocking Pink"),
        ("A0522D", "Sienna"),
        ("C0C0C0", "Silver"),
        ("87CEEB", "Sky Blue"),
        ("708090", "Slate Greyy"),
        ("003399", "Smalt"),
        ("A7FC00", "Spring bud"),
        ("00FF7F", "Spring green"),
        ("4682B4", "Steel blue"),
        ("D2B48C", "Tan"),
        ("F28500", "Tangerine"),
        ("FFCC00", "Tangerine yellow"),
        ("483C32", "Taupe"),
        ("8B8589", "Taupe grey"),
        ("D0F0C0", "Tea Green"),
        ("F88379", "Tea rose"),
        ("F4C2C2", "Tea rose"),
        ("008080", "Teal"),
        ("CD5700", "Tawny"),
        ("E2725B", "Terra cotta"),
        ("D8BFD8", "Thistle"),
        ("DE6FA1", "Thulian pink"),
        ("FF6347", "Tomato"),
        ("30D5C8", "Turquoise"),
        ("66023C", "Tyrian purple"),
        ("120A8F", "Ultramarine"),
        ("FF6FFF", "Ultra pink"),
        ("5B92E5", "United Nations blue"),
        ("AE2029", "Upsdell red"),
        ("C5B358", "Vegas Gold"),
        ("C80815", "Venetian red"),
        ("E34234", "Vermilion"),
        ("8B00FF", "Violet"),
        ("EE82EE", "Violet"),
        ("8601AF", "Violet"),
        ("40826D", "Viridian"),
        ("F5DEB3", "Wheat"),
        ("FFFFFF", "White"),
        ("C9A0DC", "Wisteria"),
        ("738678", "Xanadu"),
        ("0F4D92", "Yale Blue"),
        ("FFFF00", "Yellow"),
        ("FFEF00", "Yellow"),
        ("FEFE33", "Yellow"),
        ("9ACD32", "Yellow-green"),
    ]

    ordinary_list = [
        "cross",
        "pale",
        "fess",
        "bend",
        "chevron",
        "saltire",
        "chief",
    ]

    def design(self, profile):
        """
        Performs the design of the shield given a particular profile. Currently,
        this hands of to pick_colours to design the colours based on the family
        name.
        """

        shield = dict()

        if profile.has_key("family_name"):
            shield["ordinary"] = self.pick_ordinary(profile["family_name"])

            shield["fur"], shield["tincture"] = self.pick_colours(
                profile["family_name"]
            )

        return shield

    def pick_colours(self, seed):
        """
        Takes a string seed and returns two random colours.
        """

        hash_num = int(hashlib.sha1(seed).hexdigest(), 16)
        colour_count = len(self.colourlist)

        colour1_hex, colour1_name = self.colourlist[hash_num % colour_count]
        hash_num = hash_num / colour_count
        colour2_hex, colour2_name = self.colourlist[hash_num % colour_count]

        return (
            dict(hex=colour1_hex, name=colour1_name),
            dict(hex=colour2_hex, name=colour2_name),
        )

    def pick_ordinary(self, seed):
        """
        Takes a string seed and returns a random ordinary.
        """

        hash_num = int(hashlib.sha1(seed).hexdigest(), 16)
        ordinary_count = len(self.ordinary_list)
        return self.ordinary_list[hash_num % ordinary_count]
