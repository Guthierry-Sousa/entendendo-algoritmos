#include <stdio.h>

#define TAM 15

int main(){

    int min, aux;
    int arr[TAM] = {10, 3, 4, 10, 5, 6, -1, 1000, 3, 4, 10, 2, 10, 99, -10};

    for(int i = 0; i<TAM-1; i++){

        min = i;

        for(int j = i+1; j<TAM; j++){

            if (arr[j] < arr[min]){
                min = j;
            }
        }

        if(min != i){
            aux = arr[i];
            arr[i] = arr[min];
            arr[min] = aux;
        }

    }

    for(int z = 0; z < TAM; z++){
        printf("arr[%d] = %d\n", z, arr[z]);
    }

    return 0;
}