n = int(input('Digite um número inteiro para fazer a conversão: '))
print('Agora, escolha uma das bases de conversão abaixo\n'
      '1) BINÁRIO\n'
      '2) OCTAL\n'
      '3) HEXADECIMAL')
option = int(input('Sua opção: '))
if option == 1:
    print('{} convertido para BINÁRIO é {}.'.format(n, bin(n)[2:]))
elif option == 2:
    print('{} convertido para OCTAL é {}.'.format(n, oct(n)[2:]))
elif option == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(n, hex(n)[2:]))
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')