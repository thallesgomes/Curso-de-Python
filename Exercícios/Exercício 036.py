valor = float(input('Qual o valor da casa? R$ '))
salário = float(input('Quanto é o salário do comprador? R$ '))
anos = int(input('Em quantos pretende pagar? '))
prestação = valor / (anos * 12)
mínimo = salário * 0.3
print('Para pagar uma casa de R$ {:.2f}, em {} anos, a prestação será de R$ {:.2f}.'.format(valor, anos, prestação))
if prestação <= mínimo:
    print('O empréstimo pode ser aprovado!')
else:
    print('Infelizmente, o empréstimo não pode ser aprovado!')