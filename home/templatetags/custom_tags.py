from django import template


register = template.Library()


@register.filter(name= 'truncate_char')
def truncate_chars(value, num_chars):
    if len(value) <= num_chars:
        return value
    return value[:num_chars] + '...'