print("\n \033[1;7;30m   {:=^150}   \033[m \n".format("  |   EXERCÍCIO PYTHON 059 - CRIANDO UM MENU DE OPÇÕES   |  "))
# ================================================================================================================================================================================================================ #
'''from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('\n[ 1 ] somar\n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior\n'
          '[ 4 ] novos números\n'
          '[ 5 ] sair do programa\n')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('\nA soma de {} + {} é {}.\n'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('\nO resultado de {} x {} é {}.\n'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('\nEntre {} e {} o maior é {}.\n'.format(n1, n2, maior))
    elif opção == 4:
        print('\nInforme os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('\nFinalizando...\n')
    else:
        print('Opção inválida. Tente novamente,')
    print('=-=' * 10)
sleep(2)
print('Fim do programa! Volte sempre!')'''
# ================================================================================================================================================================================================================ #
'''n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    opção = int(input('\n1) somar\n2) multiplicar\n3) maior\n4) novos números\n5) sair do programa\n\n>>>>> Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('\nA soma de {} + {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('\nO resulto de {} x {} é {}.'.format(n1, n2, produto))
    elif opção == 3:
        maior = n2
        if n1 > n2:
            maior = n1
        print('\nEntre {} e {} o maior é {}.'.format(n1, n2, maior))
    elif opção == 4:
        n1 = int(input('\nPrimeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('\nFim do programa! Volte sempre!')
    else:
        print('\nOpção inválida. Tente novamente,')'''
# ================================================================================================================================================================================================================ #
'''n1 = int(input('Enter the 1th value: '))
n2 = int(input('Enter the 2th value: '))
option = int(input('\n1) Sum\n2) Multiply\n3) See the highest number\n4) Enter new values\n5) Exit program\n\nNow, enter the number corresponding to the action you want. What do you want to do: '))
while str(option) in '12345' and option != 5:
    if option == 1:
        print('\n{} + {} is equal to {}.'.format(n1, n2, n1 + n2))
    if option == 2:
        print('\n{} x {} is equal to {}.'.format(n1, n2, n1 * n2))
    if option == 3:
        if n1 == n2:
            print('\nThe numbers you entered are the same.')
        else:
            high = n1
            if n2 > n1:
                high = n2
            print('\nBetween {} and {}, the highest is {}.'.format(n1, n2, high))
    if option == 4:
        n1 = int(input('\nNew 1th value: '))
        n2 = int(input('New 2th value: '))
    option = int(input('\n1) Sum\n2) Multiply\n3) See the highest number\n4) Enter new values\n5) Exit program\n\nAnd now, wat do you wanna do? '))
while str(option) not in '12345':
    option = int(input('\nInvalid option! Please, try again: '))
print('\nGoodbye... See you later...')'''
# ================================================================================================================================================================================================================ #
