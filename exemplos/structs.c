// tests/structs.c

// Definição global da struct
struct Ponto {
    int x;
    float y;
};

int main() {
    // Declaração de uma instância da struct
    struct Ponto p1;
    int x_val;

    // Atribuindo valores aos membros da struct
    p1.x = 10;
    p1.y = 20.5;

    // Acessando um valor de um membro da struct
    x_val = p1.x;

    printf("Struct utilizada com sucesso.");

    return 0;
}