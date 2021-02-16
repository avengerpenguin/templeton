"""
Classes for extracting profile information from Facebook.
"""

from templeton.extract.core import BaseExtractor
from templeton.util.facebook import GraphAPI


class FacebookExtractor(BaseExtractor):
    """
    A profile information extractor that returns information from a Facebook
    profile given a username.
    """

    FIELD_MAPPINGS = [
        ("family_name", "last_name"),
        ("full_name", "name"),
        ("sex", "gender"),
        ("locale", "locale"),
    ]

    def __init__(self, oauth_access_token=None):
        super().__init__()
        self.api = GraphAPI(oauth_access_token)

    def extract(self):
        username = self.get_config("username")
        data = self.api.get_object(username)

        profile = dict()
        for profile_field, fb_field in self.FIELD_MAPPINGS:
            if data.has_key(fb_field):
                profile[profile_field] = data[fb_field]

        return profile
