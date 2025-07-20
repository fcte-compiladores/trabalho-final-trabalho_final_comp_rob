// tests/bubble_sort.c

int main() {
    int numeros[5];
    numeros[0] = 5;
    numeros[1] = 1;
    numeros[2] = 4;
    numeros[3] = 2;
    numeros[4] = 3;

    int tamanho = 5;
    int i = 0;
    int j = 0;
    int temp;

    // Lógica do Bubble Sort
    while (i < tamanho) {
        j = 0;
        while (j < tamanho - i - 1) {
            if (numeros[j] > numeros[j+1]) {
                // Troca os elementos
                temp = numeros[j];
                numeros[j] = numeros[j+1];
                numeros[j+1] = temp;
            }
            j = j + 1;
        }
        i = i + 1;
    }

    // Para ver o resultado, teríamos que melhorar o printf
    // ou inspecionar a variável 'numeros' no código Python gerado.
    printf("Array ordenado!");

    return 0;
}