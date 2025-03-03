# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='split_newline')
def split_newline(value):
    # Memisahkan string berdasarkan baris baru (\n)
    return value.split('\n')