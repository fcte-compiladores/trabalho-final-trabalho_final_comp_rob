import sys
from src.lexer import lexer
from src.parser import parser
from src.code_generator import CodeGenerator

def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <caminho_para_o_arquivo.c>")
        sys.exit(1)
    filepath = sys.argv[1]
    try:
        with open(filepath, 'r') as file:
            source_code = file.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em '{filepath}'")
        sys.exit(1)
    print("--- Iniciando compilação ---")
    ast = parser.parse(source_code, lexer=lexer)
    if not ast:
        print("--- Compilação falhou devido a erros de sintaxe. ---")
        return
    print("--- Análise sintática concluída. AST gerada. ---")
    print("--- Gerando código Python... ---")
    generator = CodeGenerator()
    python_code = generator.generate_code(ast)
    print("\n--- CÓDIGO PYTHON GERADO ---\n")
    print(python_code)
    print("\n------------------------------\n")
    output_filename = filepath.replace('.c', '.py')
    with open(output_filename, 'w') as out_file:
        out_file.write(python_code)
    print(f"Código salvo em '{output_filename}'")

if __name__ == '__main__':
    main() 