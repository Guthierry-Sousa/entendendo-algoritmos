# A checagem por duplicatas é realizada muito rapidamente com o uso de uma tabela hash

from time import sleep

def verificar_voto(nome: str, votaram: dict) -> bool:

    if votaram.get(nome):

        return True
    
    else:

        return False
    
votaram = {}

votaram['Elis'] = True
votaram['Guthierry'] = True
votaram['Elen'] = True

nome = input("Informe seu nome: ")

if verificar_voto(nome, votaram):

    print(f"{nome} já votou. Dispensado!\n")

else:
    print("Pode ir votar!")
    print("Votando...")
    sleep(2)
    print(f"{nome} votou com sucesso!")
    votaram[nome] = True

print(votaram)

