def tamanho_maior_substring(string: str) -> int:

    len_max = 1
    count = 1
    verificados = set()

    for i in range(len(string)-1):

        if (string[i] != string[i+1]) and (string[i+1] not in verificados):

            count += 1
            verificados.add(string[i])

            if count > len_max:

                len_max = count

        else:

            count = 1

    return len_max

string1 = 'abcabcbb'
string2 = 'bbbb'

print(tamanho_maior_substring(string1))
print(tamanho_maior_substring(string2))
