def mdc_euclides(a: int, b: int) -> int:

    if (b == 0) and (a == 0):

        return None
    
    if b == 0:

        return a
    
    return mdc_euclides(b, a%b)

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))

result = mdc_euclides(a, b)

if result:

    print(f"MDC({a}, {b}) = {result}")
        
else:

    print("Parâmetros Inválidos!")