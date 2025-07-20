// tests/operadores_avancados.c
int main() {
    int a = 10;
    int b = 20;
    int c;

    // Teste: Atribuição Composta
    a += 5; // a se torna 15

    // Teste: Incremento
    b++; // b se torna 21

    // Teste: Operador Ternário
    c = a > b ? 100 : 200; // a (15) não é > b (21), então c se torna 200

    // Teste: Operadores Bitwise
    int x = 5;  // Binário: 0101
    int y = 3;  // Binário: 0011
    int z;
    z = x & y;  // z se torna 1 (0001)

    printf("Testes concluidos.");
    return 0;
}