# Utilizando recursão: quando uma função chame a si mesma. 

def procure_pela_chave(caixa_principal: list[list]):

    for item in caixa_principal:

        if isinstance(item, list):

            procure_pela_chave(item) # -> Recursão

        elif item == 'chave':

            print("Encontrei a chave!")

            return

caixa_principal = [[1,2,3], [[[["chave"]]]] ,[[[4,5]]],[[[0]]], ["guthy"]]

procure_pela_chave(caixa_principal=caixa_principal)