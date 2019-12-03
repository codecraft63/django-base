from django import template
from django.conf import settings


register = template.Library()


def get_gtm_id():
    return settings.GTM_ID

@register.inclusion_tag('utils/gtm.html')
def gtm(noscript=False):
    return {
        'noscript': noscript,
        'gtm_id': get_gtm_id()
    }
