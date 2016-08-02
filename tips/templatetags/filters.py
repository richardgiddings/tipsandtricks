from django import template

register = template.Library()

@register.filter
def for_tip(tricks, tip):
    return tricks.filter(tip=tip)