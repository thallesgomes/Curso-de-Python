print('\n\033[1;7;30m {:=^150} \033[m\n\n'.format(' | EXERCÍCIO PYTHON 060 - CÁLCULO DO FATORIAL | '))
# ================================================================================================================================================================================================================ #
'''n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}.'.format(f))'''
# ================================================================================================================================================================================================================ #
"""from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
print('Calculando 5!... O fatorial de {} é igual a {}.'.format(n, factorial(n)))"""
# ================================================================================================================================================================================================================ #
'''n = int(input('Digite um número para calcular seu Fatorial: '))
f = 1
print('Calculando {}! = '.format(n), end='')
while n > 0:
    print('{}'.format(n), end=''), print(' x ' if n > 1 else ' = ', end='')
    f *= n
    n -= 1
print('{}.'.format(f))'''
# ================================================================================================================================================================================================================ #
'''n = int(input('Deseja calcular o fatorial de que número? '))
f = 1
print(f'\nCalculando o fatorial de {n}...\n{n}! =', end=' ')
for z in range(n, 0, -1):
    print(f'{z}', end=' '), print('x' if z > 1 else '=', end=' ')
    f *= z
print(f)'''