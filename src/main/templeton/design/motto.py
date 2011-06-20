from templeton.design.core import BaseDesigner

class MottoDesigner(BaseDesigner):
    def design(self, profile):
        if profile.has_key('family_name'):
            return profile['family_name']
        else:
            return None
