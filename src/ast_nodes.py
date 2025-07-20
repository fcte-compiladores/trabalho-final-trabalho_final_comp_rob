class ProgramNode:
    def __init__(self, functions):
        self.functions = functions
class FunctionNode:
    def __init__(self, return_type, name, params, body):
        self.return_type = return_type
        self.name = name
        self.params = params
        self.body = body
class BlockNode:
    def __init__(self, statements):
        self.statements = statements
class VarDeclarationNode:
    def __init__(self, var_type, var_name, value):
        self.var_type = var_type
        self.var_name = var_name
        self.value = value
class AssignNode:
    def __init__(self, var_name, value):
        self.var_name = var_name
        self.value = value
class ReturnNode:
    def __init__(self, value):
        self.value = value
class PrintfNode:
    def __init__(self, format_string, args):
        self.format_string = format_string
        self.args = args
class ScanfNode:
    def __init__(self, format_string, variables):
        self.format_string = format_string
        self.variables = variables
class IfNode:
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block
class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
class NumberNode:
    def __init__(self, value):
        self.value = value
class StringNode:
    def __init__(self, value):
        self.value = value
class IdNode:
    def __init__(self, name):
        self.name = name
class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
class ArrayDeclarationNode:
    def __init__(self, var_type, var_name, size):
        self.var_type = var_type
        self.var_name = var_name
        self.size = size
class ArrayAccessNode:
    def __init__(self, var_name, index):
        self.var_name = var_name
        self.index = index
class ParamNode:
    def __init__(self, var_type, var_name):
        self.var_type = var_type
        self.var_name = var_name
class FunctionCallNode:
    def __init__(self, func_name, args):
        self.func_name = func_name
        self.args = args
class ForNode:
    def __init__(self, init, condition, increment, body):
        self.init = init
        self.condition = condition
        self.increment = increment
        self.body = body
class FloatNode:
    def __init__(self, value):
        self.value = value
class CharNode:
    def __init__(self, value):
        self.value = value
class StructDefNode:
    def __init__(self, name, members):
        self.name = name
        self.members = members
class MemberAccessNode:
    def __init__(self, struct_var, member):
        self.struct_var = struct_var
        self.member = member
class TernaryOpNode:
    def __init__(self, condition, true_expr, false_expr):
        self.condition = condition
        self.true_expr = true_expr
        self.false_expr = false_expr
class UpdateNode:
    def __init__(self, var, op):
        self.var = var
        self.op = op
class UnaryOpNode:
    def __init__(self, op, expression):
        self.op = op
        self.expression = expression
class DoWhileNode:
    def __init__(self, body, condition):
        self.body = body
        self.condition = condition