print('\n\033[1;7;30m {:=^150} \033[m\n'.format(' | EXERCÍCIO PYTHON 014 - VALIDAÇÃO DE DADOS | '))
# ==================================================================================================================================================================================================================== #
for z in range(0, 1000):
    sexo = str(input('\033[30mInforme seu sexo: (M/F)\033[m ')).strip().upper()[0]
    if sexo not in 'MF':    # if sexo != 'M' and sexo != 'F'
        print('\033[1;31mDados inválidos! Tente novamente!\033[m\n')
    if sexo in 'MF':      # 1ª forma: if sexo in 'MF':      # 2ª forma: if sexo == 'M' or sexo == 'F':
        print('\033[1;34mValidação realizada com sucesso! Sexo \033[1;30m"{}"\033[1;34m registrado.'.format(sexo))
        break
# ==================================================================================================================================================================================================================== #
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('\033[30mInforme o seu sexo (M/F):\033[m ')).strip().upper()[0]
    if sexo not in 'MF':
        print('\033[1;31mOpção inválida! Tente novamente!\033[m\n')
    else:
        print('\033[1;33mValidação de dados concluída com sucesso. Sexo \033[1;30m"{}"\033[1;33m registrado.\033[m'.format(sexo))
# ==================================================================================================================================================================================================================== #
sexo = str(input('\033[30mInforme o seu sexo (M/F):\033[m ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('\033[1;31mDados inválidos.\033[m \033[30mPor favor, informe o seu sexo (M/F):\033[m ')).strip().upper()[0]
print('\033[1;32mValidação concluída! Sexo \033[1;30m"{}"\033[1;32m registrado.\033[m'.format(sexo))
# ==================================================================================================================================================================================================================== #
