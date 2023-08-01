from django import template

register = template.Library()


def currenc(amount):
    return '{:.2f}'.format(amount) + '$'


register.filter('currency', currenc)











