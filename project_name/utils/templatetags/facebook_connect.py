from django import template, settings

register = template.Library()

def get_facebook_app_id():
    return settings.env('FACEBOOK_APP_ID', default=False)

@register.inclusion_tag('utils/facebook_connect.html')
def facebook_connect_tag():
    try:
        return {'id': get_facebook_app_id()}
    except:
        return {}



