tabela_hash = [[] for _ in range(10)]

def funcao_hash(chave: str) -> int:

    sum_char = 0

    for char in chave:

        sum_char += ord(char)

    return sum_char % 10

def add(chave: str):

    idx = funcao_hash(chave)

    tabela_hash[idx].append(chave)

def search(chave: str):

    idx = funcao_hash(chave)

    if len(tabela_hash[idx]) != 0:

        for i in tabela_hash[idx]:

            return i == chave
        
    return False

def delete(chave: str):

    idx = funcao_hash(chave)

    for i in range(len(tabela_hash[idx])):

        if tabela_hash[idx][i] == chave:

            del tabela_hash[idx][i]


add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')

print(tabela_hash)

print("'Bob' is in the Hash Table:", search('Bob'))

delete('Stuart')
add('Bob')

print(tabela_hash)


