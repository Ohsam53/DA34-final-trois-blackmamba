from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

# 게시판 순서 1,2,3,4,5,6 등 순서 조정, 장고 책페이지 p138