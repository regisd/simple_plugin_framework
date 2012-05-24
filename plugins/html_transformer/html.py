#/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Régis Décamps'
import mount_point
class HtmlTransformer(mount_point.TextTransformer):
    ''' Plugin to wrap text in a html tag
    '''

    def __init__(self, program):
        self.tag = None

    # As documented in the Mount point, this method must be implemented
    def transform_text(self, string):
        if self.tag:
            return "<{tag}>{original}</{tag}>".format(tag=self.tag, original=string)
        else:
            return string


class HtmlEmTransformer(HtmlTransformer):
    ''' Wraps text in a ``em``tag.
    '''

    def __init__(self, program):
        ''' This TextTransformer will transform ``string`` into ``<em>string</em>``
        '''
        self.tag = "em"


class HtmlBoldTransformer(HtmlTransformer):
    ''' Wraps text in a ``b``tag
    '''

    def __init__(self, program):
        ''' This TextTransformer will transform ``string`` into ``<b>string</b>``
        '''
        self.tag = "b"
