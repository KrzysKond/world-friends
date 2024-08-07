from django import template
from datetime import datetime

register = template.Library()


@register.filter(name='calculate_age')
def calculate_age(birth_year):
    if birth_year:
        current_year = datetime.now().year
        return current_year - int(birth_year)
    return ''
