#include <stdio.h>

int main(){

    int tam = 4;

    int array[5] = {1, 2, 3, 4};

    printf("Elemento na posição 2: %d\n", array[2]);

    int novo_elemento = 10;
    int idx_novo_elemento = 2;

    for(int i = tam; i > idx_novo_elemento; i--){

        array[i] = array[i-1];

    }

    array[idx_novo_elemento] = novo_elemento;
    tam++;

    printf("Array apos insercao: ");
    for (int i = 0; i < tam; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    return 0;
}