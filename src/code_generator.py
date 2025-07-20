from src import ast_nodes
import re
class CodeGenerator:
    def __init__(self):
        self.indentation_level = 0
    def _make_indent(self):
        return "    " * self.indentation_level
    def generate_code(self, node):
        print(f'[DEBUG] generate_code chamado com node: {type(node).__name__}')
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)
    def generic_visit(self, node):
        raise Exception(f'Nenhum método visit_{type(node).__name__} encontrado')
    def visit_ProgramNode(self, node):
        print(f'[DEBUG] visit_ProgramNode: node.functions = {node.functions}')
        return "\n\n".join(self.generate_code(decl) for decl in node.functions)
    def visit_StructDefNode(self, node):
        class_name = self.generate_code(node.name)
        code = f"class {class_name}:\n"
        code += "    def __init__(self):\n"
        if not node.members:
            code += "        pass"
            return code
        for member in node.members:
            member_name = self.generate_code(member.var_name)
            code += f"        self.{member_name} = None\n"
        return code.strip()
    def visit_MemberAccessNode(self, node):
        struct_var_code = self.generate_code(node.struct_var)
        member_code = self.generate_code(node.member)
        return f"{struct_var_code}.{member_code}"
    def visit_VarDeclarationNode(self, node):
        var_name = self.generate_code(node.var_name)
        indent = self._make_indent()
        if isinstance(node.var_type, tuple) and node.var_type[0] == 'struct':
            struct_name = node.var_type[1]
            return f"{indent}{var_name} = {struct_name}()"
        if node.value:
            value = self.generate_code(node.value)
            return f"{indent}{var_name} = {value}"
        else:
            return f"{indent}{var_name} = None"
    def visit_FunctionNode(self, node):
        func_name = self.generate_code(node.name)
        params_list = [self.generate_code(param) for param in node.params]
        params_str = ", ".join(params_list)
        self.indentation_level += 1
        body_code = "\n".join(self.generate_code(stmt) for stmt in node.body.statements)
        self.indentation_level -= 1
        func_declaration = f"def {func_name}({params_str}):\n{body_code}"
        if func_name == "main":
            return f"{func_declaration}\n\nif __name__ == \"__main__\":\n    main()"
        else:
            return func_declaration
    def visit_ParamNode(self, node):
        return self.generate_code(node.var_name)
    def visit_FunctionCallNode(self, node):
        func_name = self.generate_code(node.func_name)
        args_list = [self.generate_code(arg) for arg in node.args]
        args_str = ", ".join(args_list)
        return f"{func_name}({args_str})"
    def visit_BlockNode(self, node):
        self.indentation_level += 1
        statements_code = "\n".join(self.generate_code(stmt) for stmt in node.statements)
        self.indentation_level -= 1
        return statements_code
    def visit_AssignNode(self, node):
        var_name = self.generate_code(node.var_name)
        value = self.generate_code(node.value)
        indent = self._make_indent()
        return f"{indent}{var_name} = {value}"
    def visit_ReturnNode(self, node):
        value = self.generate_code(node.value)
        indent = self._make_indent()
        return f"{indent}return {value}"
    def visit_PrintfNode(self, node):
        indent = self._make_indent()
        format_string_node = node.format_string
        args = [self.generate_code(arg) for arg in node.args]
        format_string = format_string_node.value
        f_string = re.sub(r'%[dfsc]', '{}', format_string)
        if args:
            return f'{indent}print(f"{f_string}".format({", ".join(args)}))'
        else:
            return f'{indent}print("{format_string}")'
    def visit_ScanfNode(self, node):
        indent = self._make_indent()
        format_string = node.format_string.value
        vars_to_scan = [self.generate_code(var) for var in node.variables]
        specifiers = re.findall(r'%[dfsc]', format_string)
        code = []
        for i, spec in enumerate(specifiers):
            var_name = vars_to_scan[i]
            prompt = f'"{var_name}: "'
            if spec == '%d':
                code.append(f'{indent}{var_name} = int(input({prompt}))')
            elif spec == '%f':
                code.append(f'{indent}{var_name} = float(input({prompt}))')
            else:
                code.append(f'{indent}{var_name} = input({prompt})')
        return "\n".join(code)
    def visit_IfNode(self, node):
        condition = self.generate_code(node.condition)
        indent = self._make_indent()
        if_block = self.generate_code(node.if_block)
        code = f"{indent}if {condition}:\n{if_block}"
        if node.else_block:
            indent_else = self._make_indent()
            else_block = self.generate_code(node.else_block)
            code += f"\n{indent_else}else:\n{else_block}"
        return code
    def visit_BinOpNode(self, node):
        left = self.generate_code(node.left)
        right = self.generate_code(node.right)
        op = node.op
        if op == '&&': op = 'and'
        if op == '||': op = 'or'
        return f"({left} {op} {right})"
    def visit_UnaryOpNode(self, node):
        expr_code = self.generate_code(node.expression)
        if node.op == '!':
            return f"(not {expr_code})"
        return f"({node.op}{expr_code})"
    def visit_NumberNode(self, node):
        return str(node.value)
    def visit_StringNode(self, node):
        return f'"{node.value}"'
    def visit_IdNode(self, node):
        return node.name
    def visit_WhileNode(self, node):
        condition = self.generate_code(node.condition)
        indent = self._make_indent()
        body = self.generate_code(node.body)
        return f"{indent}while {condition}:\n{body}"
    def visit_ArrayDeclarationNode(self, node):
        var_name = self.generate_code(node.var_name)
        size = self.generate_code(node.size)
        indent = self._make_indent()
        return f"{indent}{var_name} = [0] * {size}"
    def visit_ArrayAccessNode(self, node):
        var_name = self.generate_code(node.var_name)
        index = self.generate_code(node.index)
        return f"{var_name}[{index}]"
    def visit_ForNode(self, node):
        indent = self._make_indent()
        init_code = self.generate_code(node.init)
        condition_code = self.generate_code(node.condition)
        self.indentation_level += 1
        body_code = self.generate_code(node.body)
        increment_code = self.generate_code(node.increment)
        increment_indent = self._make_indent()
        full_body = f"{body_code}\n{increment_indent}{increment_code}"
        self.indentation_level -= 1
        return f"{init_code}\n{indent}while {condition_code}:\n{full_body}"
    def visit_FloatNode(self, node):
        return str(node.value)
    def visit_CharNode(self, node):
        return f"'{node.value}'"
    def visit_TernaryOpNode(self, node):
        cond_code = self.generate_code(node.condition)
        true_code = self.generate_code(node.true_expr)
        false_code = self.generate_code(node.false_expr)
        return f"({true_code} if {cond_code} else {false_code})"
    def visit_UpdateNode(self, node):
        var_code = self.generate_code(node.var)
        indent = self._make_indent()
        if node.op == '++':
            return f"{indent}{var_code} += 1"
        else:
            return f"{indent}{var_code} -= 1"
    def visit_DoWhileNode(self, node):
        indent = self._make_indent()
        self.indentation_level += 1
        body_code = self.generate_code(node.body)
        self.indentation_level -= 1
        cond_code = self.generate_code(node.condition)
        return (f"{indent}while True:\n"
                f"{body_code}\n"
                f"{indent}    if not ({cond_code}):\n"
                f"{indent}        break")