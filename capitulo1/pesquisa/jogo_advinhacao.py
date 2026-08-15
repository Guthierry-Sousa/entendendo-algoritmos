import random as rd

def advinhacao():

    numero_sorteado = rd.randint(1, 101)

    print("\n--------------------JOGO DA ADVINHAÇÃO--------------------\n")
    print("ESTOU PENSANDO EM UM NÚMERO ENTRE 1 E 100, TENTE ADVINHAR!\n")

    while(True):

        chute = int(input("Informe um número: "))

        if chute == numero_sorteado:

            print(f"Você acertou. O número sorteado foi: {numero_sorteado}")

            break

        elif chute > numero_sorteado:

            print("Informe um número menor.\n")

        else:

            print("Informe um número maior.\n")

advinhacao()

