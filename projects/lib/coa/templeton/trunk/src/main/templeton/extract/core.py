"""
Classes that define global behaviour for all profile extractors.
"""

class BaseExtractor(object):
    """
    Base abstract class for defining functions common to all profile extractors.
    """

    def __init__(self):
        self.config = {}

    def set_config(self, key, value):
        """
        Sets a key-value pair for the purposes of configuring the extractor in
        ways that may be relevant to particular subclasses.
        """
        self.config[key] = value

    def get_config(self, key):
        """
        Fetches a config value by key which may be useful to subclasses that
        require configuration.
        """
        if (self.config.has_key(key)):
            return self.config[key]
        else:
            raise ConfigNotSetError(key)

    def extract(self):
        """
        The main method for extracting profile information. This is not
        implemented and thus remains abstract in this base class. It must be
        overridden in a subclass to extract information in some way.
        """
        raise NotImplementedError(
            """This extractor doesn't know how to extract. Please override
extract() method in subclass."""
            )


class ConfigNotSetError(Exception):
    """
    An error which is thrown by any extractor when a config value is asked for,
    but hasn't been set yet. This ensures no extractor subclass can be used
    before being correctly configured.
    """

    def __init__(self, key):
        super(ConfigNotSetError, self).__init__() 
        self.message = u'Config not set: %s' % key

    def __unicode__(self):
        return self.message

    def __str__(self):
        return unicode(self)
