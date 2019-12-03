from django.utils.text import slugify


def path(instance, filename, entity_name=None, ident=None, path=None):
    if not entity_name:
        entity_name = slugify(instance.__class__.__name__)

    if not ident:
        if not instance:
            pattern = "{entity}/common/"
        else:
            pk = 'undefined'
            try:
                pk = str(instance.pk) if instance.pk else str(instance.variant.pk)
            except:
                pass
            pattern = "{entity}/" + pk + "/"
    else:
        pattern = "{entity}/{ident}/"

    if path:
        pattern += "/{path}"

    pattern += "{filename}"

    return pattern.format(
        entity=entity_name,
        ident=ident,
        filename=filename,
        path=path
    )
