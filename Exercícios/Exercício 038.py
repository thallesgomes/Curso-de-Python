n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
if n1 > n2:
    print(f'{n1} é maior que {n2}.')
elif n2 > n1:
    print(f'{n2} é maior que {n1}.')
elif n1 == n2:
    print('Os dois valores são igual!')