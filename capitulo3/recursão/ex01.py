def substituir_digitos_impares(num):

    num_str = str(num)

    if len(num_str) == 0:
        return ""

    else:

        if int(num_str[0])%2 == 0:

            return num_str[0] + substituir_digitos_impares((num_str[1:]))

        else:

            return '6' + substituir_digitos_impares((num_str[1:]))


print(substituir_digitos_impares(425))