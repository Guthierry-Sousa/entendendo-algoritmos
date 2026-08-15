#include <stdio.h>

void greet(char *nome);
void greet2(char *nome);
void bye();

int main(int argc, char **argv){

    if(argc == 1){
        greet("Maggie");
        return 0;
    }

    greet(argv[1]);

    return 0;
}

void greet(char *nome){
    printf("Salve, %s!\n", nome);
    greet2(nome);
    printf("Preparando para dizer tchau . . .\n");
    bye();

}

void greet2(char *nome){
    printf("Como vai, %s?\n", nome);
}

void bye(){
    printf("Ok, bye bye!\n");
}