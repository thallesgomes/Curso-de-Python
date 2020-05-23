print('\n\033[1;7;30m   {:=^150}   \033[m\n'.format('  |   EXERCÍCIO PYTHON 058 - JOGO DA ADVINHAÇÃO (2.0)   |  '))
# ========================================================================================================================= #
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
# ========================================================================================================================= #
from random import randint
computer = randint(0, 10)
print('34mHi! I am your computer...\nI just thought of a number between 0 and 10. Can you guess wich number i thought?')
guesses = 0
corret = False
while not corret:
    player = int(input('\nWhat is your guess? '))
    guesses += 1
    if player == computer:
        corret = True
    elif player < computer:
        print('Wrong... try a higher number...')
    elif player > computer:
        print('Wrong... try a lower number...')
print('You are right! Nice! You tried {} times.'.format(guesses))
# ========================================================================================================================= #
from random import randint
computer = randint(0, 10)
player = int(input("Hi! I'm your computer!\nI thought of a number between 0 and 10. Can you guess which number is it?\n\nWhat's your guess? "))
guesses = 1
while player != computer:
    if player < computer:
        player = int(input("Try again with a higher number: "))
    elif player > computer:
        player = int(input("Try again with a lower number: "))
    guesses += 1
print("\nCongratulations! You got it right in {} attempts!".format(guesses))
# ========================================================================================================================= #from random import randint
computer = randint(0, 10)
player = int(input("Let's play a little game.\nI'll think of a number between 0 and 10.\n\nTry to guess: "))
guesses = 1
while player != computer:
    print("You missed! Try again: ")
    guesses += 1
print('Very nice! You got it right in {} attempts.'.format(guesses))
# ========================================================================================================================= #
