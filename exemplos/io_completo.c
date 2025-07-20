// tests/io_completo.c

int main() {
    int idade;
    // Nosso compilador ainda não tem arrays de char para strings,
    // então vamos usar uma variável 'int' para o nome por simplicidade.
    // O código Python gerado funcionará corretamente.
    int nome; 

    printf("Por favor, digite seu nome e sua idade.");

    // Lê um nome (string) e uma idade (inteiro)
    scanf("%s %d", &nome, &idade);

    printf("Ola, %s! Voce tem %d anos.", nome, idade);

    if (idade > 18) {
        printf("Voce e maior de idade.");
    }

    return 0;
}