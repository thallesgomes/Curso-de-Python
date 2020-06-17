from datetime import date
ano = int(input('Ano de nascimento (apenas números): '))
hoje = date.today().year
idade = hoje - ano
if idade == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos, em {hoje - (idade-18)}.\nVÁ SE ALISTAR!')
elif idade < 18:
    print(f'Você deve se alistar daqui a {18 - idade} anos, em {hoje + (18-idade)}.')