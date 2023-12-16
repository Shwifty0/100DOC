def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
    
print(add(3, 5 , 6, 6))


def calculate(n, **kwargs):
    
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
    

print(calculate(2, add =3, multiply = 5, sub = 10))