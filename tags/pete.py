import logging
import datetime
from google.appengine.ext import webapp

from google.appengine.ext.webapp import template

logging.info('pete pete pete')

register = webapp.template.create_template_register()
def pete(value, arg):
  logging.info('inside it all')
  logging.info(value)
  return value.replace(arg, '')
register.filter('bob', pete)

# def do_upper(parser, token):
#     nodelist = parser.parse(('endupper',))
#     parser.delete_first_token()
#     return UpperNode(nodelist)

# class UpperNode(template.Node):
#     def __init__(self, nodelist):
#         self.nodelist = nodelist
#     def render(self, context):
#         output = self.nodelist.render(context)
#         return output.upper()
