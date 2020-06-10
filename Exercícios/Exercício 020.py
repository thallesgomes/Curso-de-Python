from random import shuffle
a = input('1º aluno: ')
b = input('2º aluno: ')
c = input('3º aluno: ')
d = input('4º aluno: ')
alunos = [a, b, c, d]
shuffle(alunos)
print(f'A ordem de apresentação será a seguinte: {alunos}.')