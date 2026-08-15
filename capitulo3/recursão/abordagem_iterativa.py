# Utilizando loop - while

def procupe_pela_chave(caixa_principal: list[list]):

    pilha = []

    for item in caixa_principal:

        pilha.append(item)

    while len(pilha) != 0:

        item = pilha.pop()

        if isinstance(item, list):

            for subitem in item:
                
                pilha.append(subitem)

        elif item == "chave":
             
            print("Encontrei a chave!")

            return
             

caixa_principal = [[1,2,3],[[[4,5]]],[[[0]]], ["guthy"], [[[["chave"]]]]]

procupe_pela_chave(caixa_principal=caixa_principal)
                