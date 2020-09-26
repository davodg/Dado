from random import randint


def dado():

    x = randint(1, 6)
    return x


def jogar():

    resposta = int(input('Olá, você gostaria de jogar o dado?\n1.Sim\n2.Não\n '))
    if resposta == 1:
        resultado = dado()
        print(resultado)
    elif resposta == 2:
        print('Compreensível, tenha um ótimo dia!')
        exit()

    repeat = int(input('Deseja jogar de novo?\n1.Sim\n2.Não\n'))

    if repeat == 1:
        jogar()
    else:
        print('Obrigado por jogar!!')


jogar()
