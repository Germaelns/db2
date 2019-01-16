from django import template

register = template.Library()


@register.filter(name="login")
def login(value):
    check = 0
    for char in value:
        if char.isdigit():
            check += 1
        else:
            pass
    if check > 0:
        value = "text must be only with chars"

    return value
