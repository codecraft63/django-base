from django import template
from django.conf import settings


register = template.Library()

def get_facebook_app_id():
    return settings.FACEBOOK_ID

@register.inclusion_tag('utils/facebook_connect.html')
def facebook_connect():
    return {'id': get_facebook_app_id()}

