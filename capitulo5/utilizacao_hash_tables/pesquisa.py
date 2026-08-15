# As tabelas hash são ótimas opções quando:
# - Você deseja mapear algum item com relação a outro
# - Você precisa pesquisar algo

lista_telefonica = {
    "Ana": "99999-1111",
    "Guthy": "98888-2222",
    "Carlos": "97777-3333"
}

def buscar_contato(nome: str):
    if lista_telefonica.get(nome):
        print(f"O número de {nome} é: {lista_telefonica[nome]}")
    else:
        print(f"Contato {nome} não encontrado.")

buscar_contato("Guthy")