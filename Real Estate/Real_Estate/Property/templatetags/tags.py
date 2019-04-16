import decimal
from django import template

register = template.Library()


@register.filter
def currency_in_indian_format(n):
    """ Convert a number (int / float) into indian formatting style """

    s = str(n)

    l = len(s)
    i = l - 1

    res, flag, k = '', 1, 0
    while i >= 0:
        if flag == 1:
            k += 1
            res += s[i]
            if k == 3 and i - 1 >= 0:
                res += ','
                flag = 2
                k = 0
        else:
            k += 1
            res += s[i]
            if k == 2 and i - 1 >= 0:
                res += ','
                flag = 2
                k = 0
        i -= 1

    return res[::-1]
