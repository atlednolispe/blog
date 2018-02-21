from django import template

english = {
    1: 'one',
    2: 'two',
    3: 'three',
}

register = template.Library()


@register.filter
def mod(dividend, divisor):
    return dividend % divisor + 1


@register.filter
def mod_eng(dividend, divisor):
    return english[dividend % divisor + 1]


@register.filter
def alt_filter(dividend, divisor):
    return dividend % divisor == 0


@register.filter
def content_cut_off(content, length):
    return content[:length]


@register.filter
def subsection(content, length):
    html = ''

    while content:
        sub, content = content[:length], content[length:]
        html += '<p>%s</p>\n' % sub
    return html
