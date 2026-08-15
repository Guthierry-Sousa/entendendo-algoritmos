def menor_valor(arr: list) -> int:
    min = 0

    for i in range(1, len(arr)):

        if(arr[i] < arr[min]):

            min = i

    return min

def selection_sort(arr: list[int]) -> list[int]:
    new_arr = []

    for _ in range(len(arr)):

        idx_min_val = menor_valor(arr=arr)

        new_arr.append(arr.pop(idx_min_val))

    return new_arr

array = [10, 3, 4, 10, 5, 6, -1000, 1000, 3, 4, 10, 2, 10, 99, 2]

print(selection_sort(arr=array))