import ply.yacc as yacc
from src.lexer import tokens
from src.ast_nodes import (
    ProgramNode, FunctionNode, BlockNode, VarDeclarationNode, AssignNode,
    ReturnNode, PrintfNode, IfNode, BinOpNode, NumberNode, StringNode, IdNode,
    WhileNode, ArrayDeclarationNode, ArrayAccessNode,
    ParamNode, FunctionCallNode,
    ForNode,
    FloatNode, CharNode,
    StructDefNode, MemberAccessNode,
    ScanfNode, TernaryOpNode, UpdateNode, UnaryOpNode, DoWhileNode
)
precedence = (
    ('left', 'LOGICAL_OR'),
    ('left', 'LOGICAL_AND'),
    ('left', 'EQUALS_EQUALS', 'NOT_EQUALS'),
    ('left', 'LESS_THAN', 'GREATER_THAN', 'LESS_EQUALS', 'GREATER_EQUALS'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
)
def p_program(p):
    'program : global_declarations'
    p[0] = ProgramNode(p[1])
def p_global_declarations(p):
    '''global_declarations : global_declarations global_declaration
                           | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []
def p_global_declaration(p):
    '''global_declaration : function_definition
                          | struct_definition'''
    p[0] = p[1]
def p_struct_definition(p):
    'struct_definition : STRUCT ID LBRACE member_list RBRACE SEMICOLON'
    p[0] = StructDefNode(IdNode(p[2]), p[4])
def p_member_list(p):
    '''member_list : member_list member
                   | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []
def p_member(p):
    'member : type ID SEMICOLON'
    p[0] = VarDeclarationNode(p[1], IdNode(p[2]), None)
def p_function_definition(p):
    'function_definition : type ID LPAREN parameter_list RPAREN LBRACE block RBRACE'
    return_type = p[1]
    name = IdNode(p[2])
    params = p[4]
    body = p[7]
    p[0] = FunctionNode(return_type, name, params, body)
def p_type(p):
    '''type : INT
            | VOID
            | FLOAT
            | CHAR
            | STRUCT ID'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[1], p[2])
def p_block(p):
    'block : statements'
    p[0] = BlockNode(p[1])
def p_statements(p):
    '''statements : statements statement
                  | empty'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []
def p_statement(p):
    '''statement : declaration
                 | assignment
                 | return_statement
                 | printf_statement
                 | scanf_statement
                 | if_statement
                 | while_statement
                 | for_statement
                 | update_statement
                 | do_while_statement'''
    p[0] = p[1]
def p_declaration(p):
    '''declaration : type ID ASSIGN expression SEMICOLON
                   | type ID LBRACKET INTEGER RBRACKET SEMICOLON
                   | type ID SEMICOLON'''
    if len(p) == 6:
        p[0] = VarDeclarationNode(p[1], IdNode(p[2]), p[4])
    elif len(p) == 7:
        p[0] = ArrayDeclarationNode(p[1], IdNode(p[2]), NumberNode(p[4]))
    else:
        p[0] = VarDeclarationNode(p[1], IdNode(p[2]), None)
def p_assignment(p):
    '''assignment : ID ASSIGN expression SEMICOLON
                  | ID compound_assign_op expression SEMICOLON
                  | ID LBRACKET expression RBRACKET ASSIGN expression SEMICOLON
                  | factor DOT ID ASSIGN expression SEMICOLON'''
    if len(p) == 5:
        if p[2] == '=':
            p[0] = AssignNode(IdNode(p[1]), p[3])
        else:
            op = p[2][0]
            bin_op = BinOpNode(IdNode(p[1]), op, p[3])
            p[0] = AssignNode(IdNode(p[1]), bin_op)
    elif len(p) == 8:
        array_access = ArrayAccessNode(IdNode(p[1]), p[3])
        p[0] = AssignNode(array_access, p[6])
    else:
        struct_access = MemberAccessNode(p[1], IdNode(p[3]))
        p[0] = AssignNode(struct_access, p[5])
def p_compound_assign_op(p):
    '''compound_assign_op : PLUS_EQUALS
                          | MINUS_EQUALS
                          | TIMES_EQUALS
                          | DIVIDE_EQUALS'''
    p[0] = p[1]
def p_while_statement(p):
    'while_statement : WHILE LPAREN condition RPAREN LBRACE block RBRACE'
    p[0] = WhileNode(p[3], p[6])
def p_condition(p):
    '''condition : expression EQUALS_EQUALS expression
                 | expression NOT_EQUALS expression
                 | expression LESS_THAN expression
                 | expression GREATER_THAN expression
                 | expression LESS_EQUALS expression
                 | expression GREATER_EQUALS expression'''
    p[0] = BinOpNode(left=p[1], op=p[2], right=p[3])
def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN LBRACE block RBRACE ELSE LBRACE block RBRACE
                   | IF LPAREN expression RPAREN LBRACE block RBRACE'''
    if len(p) == 12:
        p[0] = IfNode(p[3], p[6], p[10])
    else:
        p[0] = IfNode(p[3], p[6])
def p_expression(p):
    '''expression : logical_or_expression
                 | assignment_expression'''
    p[0] = p[1]
def p_assignment_expression(p):
    'assignment_expression : ID ASSIGN expression'
    p[0] = AssignNode(IdNode(p[1]), p[3])
def p_logical_or_expression(p):
    '''logical_or_expression : logical_and_expression
                             | logical_or_expression LOGICAL_OR logical_and_expression'''
    if len(p) == 2: p[0] = p[1]
    else: p[0] = BinOpNode(p[1], p[2], p[3])
def p_logical_and_expression(p):
    '''logical_and_expression : bitwise_expression
                              | logical_and_expression LOGICAL_AND bitwise_expression'''
    if len(p) == 2: p[0] = p[1]
    else: p[0] = BinOpNode(p[1], p[2], p[3])
def p_bitwise_expression(p):
    '''bitwise_expression : additive_expression
                          | bitwise_expression BIT_OR additive_expression
                          | bitwise_expression AMPERSAND additive_expression
                          | bitwise_expression LEFT_SHIFT additive_expression'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinOpNode(p[1], p[2], p[3])
def p_additive_expression(p):
    '''additive_expression : term
                           | additive_expression PLUS term
                           | additive_expression MINUS term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinOpNode(p[1], p[2], p[3])
def p_term(p):
    '''term : factor
            | term TIMES factor
            | term DIVIDE factor
            | term MODULO factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = BinOpNode(p[1], p[2], p[3])
def p_factor(p):
    '''factor : INTEGER
              | FLOAT
              | CHAR
              | STRING
              | ID
              | ID LBRACKET expression RBRACKET
              | function_call
              | factor DOT ID
              | LOGICAL_NOT factor'''
    if p.slice[1].type == 'LOGICAL_NOT':
        p[0] = UnaryOpNode(p[1], p[2])
    else:
        slice_type = p.slice[1].type
        if len(p) == 4:
            p[0] = MemberAccessNode(p[1], IdNode(p[3]))
        elif slice_type == 'INTEGER':
            p[0] = NumberNode(p[1])
        elif slice_type == 'FLOAT':
            p[0] = FloatNode(p[1])
        elif slice_type == 'CHAR':
            p[0] = CharNode(p[1])
        elif slice_type == 'STRING':
            p[0] = StringNode(p[1])
        elif slice_type == 'ID' and len(p) == 2:
            p[0] = IdNode(p[1])
        elif len(p) == 5:
            p[0] = ArrayAccessNode(IdNode(p[1]), p[3])
        elif len(p) == 2 and not isinstance(p[1], str):
            p[0] = p[1]
def p_function_call(p):
    'function_call : ID LPAREN argument_list RPAREN'
    p[0] = FunctionCallNode(IdNode(p[1]), p[3])
def p_argument_list(p):
    '''argument_list : arguments
                     | empty'''
    p[0] = p[1] if p[1] else []
def p_arguments(p):
    '''arguments : expression
                 | arguments COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]
def p_parameter_list(p):
    '''parameter_list : parameters
                      | empty'''
    p[0] = p[1] if p[1] else []
def p_parameters(p):
    '''parameters : parameter
                  | parameters COMMA parameter'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]
def p_parameter(p):
    'parameter : type ID'
    p[0] = ParamNode(p[1], IdNode(p[2]))
def p_printf_statement(p):
    '''printf_statement : PRINTF LPAREN expression COMMA argument_list RPAREN SEMICOLON
                        | PRINTF LPAREN expression RPAREN SEMICOLON'''
    if len(p) == 8:
        p[0] = PrintfNode(p[3], p[5])
    else:
        p[0] = PrintfNode(p[3], [])
def p_scanf_statement(p):
    'scanf_statement : SCANF LPAREN expression COMMA scanf_argument_list RPAREN SEMICOLON'
    p[0] = ScanfNode(p[3], p[5])
def p_scanf_argument_list(p):
    '''scanf_argument_list : scanf_argument
                           | scanf_argument_list COMMA scanf_argument'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]
def p_scanf_argument(p):
    'scanf_argument : AMPERSAND ID'
    p[0] = IdNode(p[2])
def p_empty(p):
    'empty :'
    pass
def p_error(p):
    if p:
        print(f"Erro de sintaxe no token '{p.value}' (tipo: {p.type}) na linha {p.lineno}")
    else:
        print("Erro de sintaxe: fim inesperado do arquivo!")
def p_return_statement(p):
    '''return_statement : RETURN expression SEMICOLON
                        | RETURN SEMICOLON'''
    if len(p) == 4:
        p[0] = ReturnNode(p[2])
    else:
        p[0] = ReturnNode(None)
def p_expression_or_empty(p):
    '''expression_or_empty : expression
                          | empty'''
    p[0] = p[1]
def p_for_header_expression(p):
    '''for_header_expression : expression
                            | empty'''
    p[0] = p[1]
def p_for_relational_expression(p):
    '''for_relational_expression : ID LESS_THAN INTEGER
                                | ID GREATER_THAN INTEGER
                                | ID LESS_EQUALS INTEGER
                                | ID GREATER_EQUALS INTEGER
                                | ID EQUALS_EQUALS INTEGER
                                | ID NOT_EQUALS INTEGER
                                | expression
                                | empty'''
    if len(p) == 4:
        p[0] = BinOpNode(IdNode(p[1]), p[2], NumberNode(p[3]))
    else:
        p[0] = p[1]
def p_for_statement(p):
    '''for_statement : FOR LPAREN expression SEMICOLON for_relational_expression SEMICOLON expression RPAREN LBRACE block RBRACE'''
    p[0] = ForNode(p[3], p[5], p[7], p[10])
def p_assignment_no_semicolon(p):
    '''assignment_no_semicolon : ID ASSIGN expression
                               | ID compound_assign_op expression
                               | ID LBRACKET expression RBRACKET ASSIGN expression
                               | factor DOT ID ASSIGN expression'''
    if len(p) == 4:
        if p[2] == '=':
            p[0] = AssignNode(IdNode(p[1]), p[3])
        else:
            op = p[2][0]
            bin_op = BinOpNode(IdNode(p[1]), op, p[3])
            p[0] = AssignNode(IdNode(p[1]), bin_op)
    elif len(p) == 7:
        array_access = ArrayAccessNode(IdNode(p[1]), p[3])
        p[0] = AssignNode(array_access, p[6])
    else:
        struct_access = MemberAccessNode(p[1], IdNode(p[3]))
        p[0] = AssignNode(struct_access, p[5])
def p_for_init(p):
    '''for_init : declaration
               | assignment_no_semicolon
               | update_statement
               | empty'''
    p[0] = p[1]
def p_for_condition(p):
    '''for_condition : expression
                    | empty'''
    p[0] = p[1]
def p_for_increment(p):
    '''for_increment : expression
                    | empty'''
    p[0] = p[1]
def p_update_statement(p):
    '''update_statement : ID PLUS_PLUS SEMICOLON
                       | ID MINUS_MINUS SEMICOLON'''
    op = '++' if p[2] == '++' else '--'
    p[0] = UpdateNode(IdNode(p[1]), op)
def p_do_while_statement(p):
    'do_while_statement : DO LBRACE block RBRACE WHILE LPAREN condition RPAREN SEMICOLON'
    p[0] = DoWhileNode(p[3], p[7])
def p_expression_increment(p):
    '''expression : ID PLUS_PLUS
                  | ID MINUS_MINUS'''
    p[0] = UpdateNode(IdNode(p[1]), p[2])
parser = yacc.yacc()