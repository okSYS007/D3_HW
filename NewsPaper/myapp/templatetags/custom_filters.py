from django import template
 
register = template.Library()
 
 
@register.filter(name='multiply')  
def multiply(value, arg):
    if isinstance(value, str) and isinstance(arg, int): # проверяем, что value — это точно строка, а arg — точно число, чтобы не возникло курьёзов
        return str(value) * arg
    else:
        raise ValueError(f'Нельзя умножить {type(value)} на {type(arg)}') # в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку

@register.filter(name='Censor')  
def Censor(value, arg):

    Ban_List = [    
        "Новости",
        "lorem",
        "ipsum"
    ]
   
    return ' '.join('*'*len(i) if i.upper() in list(map(lambda x: x.upper(), Ban_List)) else i for i in value.split())