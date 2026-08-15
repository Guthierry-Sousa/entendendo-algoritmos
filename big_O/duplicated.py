def duplicated_elements(array: list, element) -> bool:

    count = 0

    for i in array:

        if i == element:

            count += 1

    if count > 1:

        return True

    return False

array = [1 ,3 ,3, 3, 5, 1, 2, 6]

print(duplicated_elements(array, 1))
print(duplicated_elements(array, 6))
print(duplicated_elements(array, 5))

def duplicated_elements2(array: list) -> bool:

    for i in array[:-1]:

        for j in array[1:]:

            if i == j:

                return True

    return False

print(duplicated_elements(array, 1))
print(duplicated_elements(array, 6))
print(duplicated_elements(array, 5))
