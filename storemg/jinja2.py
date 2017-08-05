from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    """filtro para las fechas"""
    return value.strftime(format)


def environment(**options):
    env = Environment(**options)
    env.filters['datetimeformat'] = datetimeformat
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })

    return env
