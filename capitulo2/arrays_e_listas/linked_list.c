#include <stdio.h>
#include <stdlib.h>

struct No {
    int valor;
    struct No* proximo; 
};

void imprimir_lista(struct No* no_inicial) {
    struct No* atual = no_inicial;
    while (atual != NULL) {
        printf("%d -> ", atual->valor);
        atual = atual->proximo; 
    }
    printf("NULL\n");
}

int main() {

    struct No* no1 = (struct No*)malloc(sizeof(struct No));
    struct No* no2 = (struct No*)malloc(sizeof(struct No));
    struct No* no3 = (struct No*)malloc(sizeof(struct No));

    no1->valor = 10;
    no2->valor = 20;
    no3->valor = 30;

    
    no1->proximo = no2; 
    no2->proximo = no3; 
    no3->proximo = NULL;

    printf("Lista original: ");
    imprimir_lista(no1);

    struct No* no_novo = (struct No*)malloc(sizeof(struct No));
    no_novo->valor = 25;

    no_novo->proximo = no2->proximo; 
    no2->proximo = no_novo;          

    printf("Lista apos insercao: ");
    imprimir_lista(no1);

    free(no1);
    free(no2);
    free(no_novo);
    free(no3);

    return 0;
}