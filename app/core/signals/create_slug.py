from django.template.defaultfilters import slugify


def create_slug(sender, instance, **kwargs):
    if hasattr(instance, 'slug') and not getattr(instance, 'slug'):
        slug_from = getattr(instance, 'slug_from', 'name')
        slug = slugify(getattr(instance, slug_from))
        unique_slug = slug
        num = 1
        while sender.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1

        setattr(instance, 'slug', unique_slug)
