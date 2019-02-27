from django import template, settings

register = template.Library()

def get_gtm_id():
    return settings.env('GTM_ID', default=False)

@register.inclusion_tag('utils/gtm.html')
def gtm_tag():
    try:
        return {'id': get_gtm_id()}
    except:
        return {}

@register.inclusion_tag('utils/gtm-noscript.html')
def gtm_noscript_tag:
    try:
        return {'id': get_gtm_id()}
    except:
        return {}


