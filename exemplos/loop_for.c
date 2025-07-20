// tests/loop_for.c

int main() {
    int i;
    int a = 0;

    printf("Iniciando o laco for.");

    for (i = 0; i < 5; i = i + 1) {
        a = a + 10;
        printf("Dentro do laco.");
    }

    // Ao final, no código Python, 'a' deverá ter o valor 50.
    printf("Fim do laco for.");

    return 0;
}