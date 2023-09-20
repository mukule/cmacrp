from django import template
import os

register = template.Library()

@register.filter(name='filename')
def filename(value):
    return os.path.basename(value)

@register.filter
def filename_from_path(value):
    return os.path.basename(value)

@register.filter
def filename_without_extension(value):
    # Split the file name by '.' to remove the extension
    return value.split('.')[0]
