print('\n\033[1;7;30m {:=^125} \033[m\n'.format(' | CURSO EM VÍDEO: PYTHON - AULA 14 (WHILE) | '))
# ==================================================================================================================================================================================================================== #
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\nInforme o seu sexo? (M/F) ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
    else:
        if sexo == 'M':
            print('Você é homem.')
        elif sexo == 'F':
            print('Você é mulher.')
# ==================================================================================================================================================================================================================== #
idade = 0
while idade != 18:
    idade = int(input('\nQual a idade da pessoa? '))
    if idade < 18:
        print('Essa pessoa ainda não é maior de idade.')
    elif idade == 18:
        print('Essa pessoa já pode ser considerada maior de idade.')
    else:
        print('Essa pessoa é maior de idade.')
print('\nFim!')
# ==================================================================================================================================================================================================================== #
