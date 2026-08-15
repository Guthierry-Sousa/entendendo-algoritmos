#include <stdio.h>

void pesquisa_binaria(int item, int vetor[], int len_vector);

#define TAM 10

int main(){

    int vetor[TAM] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int item;
    
    printf("Informe um número: ");
    scanf("%d", &item);

    pesquisa_binaria(item, vetor, TAM);

    return 0;
}

void pesquisa_binaria(int item, int vetor[], int len_vetor){
    int baixo = 0;
    int alto = len_vetor - 1;

    int meio;

    while(baixo <= alto){

        meio = (int) ((baixo + alto) / 2);

        if(vetor[meio] == item){
            printf("Item (%d) encontrado no índice %d\n", item, meio);
            return;
        }

        else if(item > vetor[meio]){
            baixo = meio + 1;
        }

        else{
            alto = meio - 1;
        }

    }
    printf("%d não está na lista!\n", item);

}