from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """Отримати значення зі словника за ключем"""
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    return None
