from django import template, settings

register = template.Library()


def get_gtm_id():
    return settings.env('GTM_ID', default=False)


@register.inclusion_tag('utils/gtm.html')
def gtm_tag():
    return {'id': get_gtm_id()}


@register.inclusion_tag('utils/gtm-noscript.html')
def gtm_noscript_tag:
    return {'id': get_gtm_id()}
