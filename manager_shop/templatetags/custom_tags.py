from django import template

register = template.Library()


@register.filter(name='list_index')
def list_index(mylist, index):
    return mylist[index]


