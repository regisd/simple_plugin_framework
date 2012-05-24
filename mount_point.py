import spf

__author__ = "Régis Décamps"
__doc__ = '''This module contains all mount points. A mount point is used as an interface between the program and plugins'''

class TextTransformer(object, metaclass=spf.MountPoint):
    ''' Plugins can inherit this mount point in order to modify text.

    A plugin that registers this mount point must implement the method
    * transform_text(self, string):
    '''

    def __init__(self, program):
        # Nothing is implemented here. The documentation is everything.
        pass

    def __str__(self):
        return self.__class__.__name__