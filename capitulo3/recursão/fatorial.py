def fatorial(num: int) -> int:

    if num < 0:

        return None

    elif num<=1:

        return 1
    
    else:

        return num * fatorial(num-1)

fat = fatorial(7)

print(fat)