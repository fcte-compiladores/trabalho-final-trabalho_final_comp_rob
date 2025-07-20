// tests/funcoes.c

// Função que recebe dois inteiros e retorna sua soma
int soma(int a, int b) {
    int resultado;
    resultado = a + b;
    return resultado;
}

// Função principal que chama a outra função
int main() {
    int valor1 = 20;
    int valor2 = 22;
    int total;

    // Chamando a função soma e guardando o resultado
    total = soma(valor1, valor2);

    // Infelizmente, nosso printf ainda é simples.
    // O valor de 'total' no código Python gerado será 42.
    printf("A soma foi calculada.");

    return 0;
}