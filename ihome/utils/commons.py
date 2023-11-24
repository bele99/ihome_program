# coding:utf-8

from werkzeug.routing import BaseConverter


# Defining Regular Converter
class ReConverter(BaseConverter):
    """"""
    def __init__(self, url_map, regex):
        # Calling the initialization method of the parent class
        super(ReConverter, self).__init__(url_map)
        # Save Regular Expression
        self.regex = regex
