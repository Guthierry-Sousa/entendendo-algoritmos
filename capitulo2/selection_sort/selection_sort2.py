def selection_sort(arr: list, low_to_up: bool = True) -> list:
    for i in range(len(arr)-1):

        min = i

        if low_to_up:

            for j in range(i+1, len(arr)):

                if(arr[j] < arr[min]):

                    min = j

            if(min != i):

                arr[i], arr[min] = arr[min], arr[i]

        else:

            for j in range(i+1, len(arr)):

                if(arr[j] > arr[min]):

                    min = j

            if(min != i):

                arr[i], arr[min] = arr[min], arr[i]


    return arr

array = [10, 3, 4, 10, 5, 6, -1, 1000, 3, 4, 10, 2, 10, 99, -10]

print(selection_sort(arr=array, low_to_up=False))