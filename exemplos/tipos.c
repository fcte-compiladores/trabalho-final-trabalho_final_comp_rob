// tests/tipos.c

int main() {
    int   idade = 30;
    float altura = 1.75;
    char  inicial = 'J';

    printf("Declarando variaveis de diferentes tipos.");

    float peso_ideal;
    peso_ideal = altura * altura * 22; // Operação com float

    // Imprimindo o caractere (nosso printf ainda é simples)
    if (idade > 25) {
        printf("A inicial do nome e J.");
    }
    
    return 0;
}