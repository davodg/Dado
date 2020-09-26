from random import randint


def dado():

    x = randint(1, 6)
    return x


def jogar():
    c = 'sim'

    while c == 'sim':

        try:
            resposta = input('Olá, você gostaria de jogar o dado? ')
        except TypeError:
            print("Desculpe, você digitou algo errado, tente de novo")
        if resposta == 'sim':
            resultado = dado()
            print(resultado)
        elif resposta == 'não':
            print('Compreensível, tenha um ótimo dia!')

    c = input('Você deseja jogar de novo? ')


jogar()


