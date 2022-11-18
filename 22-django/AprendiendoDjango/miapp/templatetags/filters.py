"""from django import template

register = template.library()

@register.filter(name= 'saludo')
def saludo(value):
    if len(value)>=8:
        largo='<p>Tu nombre es muy largo</p>'
    return "<h1 style='background:green;color:white;'>Bienvenido {value}</h1>" + largo

"""