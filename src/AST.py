class Node(object):
    def print_tab(self, indent):
        print("|   " * indent, end="")


class BinaryExpr(Node):
    def __init__(self, left, op, right, line):
        self.op = op
        self.left = left
        self.right = right
        self.line = line


class AssignOperation(Node):
    def __init__(self, op, left, expression):
        # print("AST AssignOperation", left)
        self.op = op
        self.left = left
        self.expression = expression


class IfCondition(Node):
    def __init__(self, cond, if_body, else_body=None):
        self.cond = cond
        self.if_body = if_body
        self.else_body = else_body


class While(Node):
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body


class For(Node):
    def __init__(self, var, begin, end, body):
        self.var = var
        self.begin = begin
        self.end = end
        self.body = body


class Break(Node):
    def __init__(self, line):
        self.line = line


class Continue(Node):
    def __init__(self, line):
        self.line = line


class Return(Node):
    def __init__(self, expr=None):
        self.expr = expr


class Print(Node):
    def __init__(self, exprs):
        self.exprs = exprs


class Transpose(Node):
    def __init__(self, arg):
        self.arg = arg


class Uminus(Node):
    def __init__(self, expression):
        self.expression = expression


class Function(Node):
    def __init__(self, function, argument):
        self.function = function
        self.arg = argument


class Matrix(Node):
    def __init__(self, new_vector, line, matrix=None):
        if matrix is not None:
            self.matrix = matrix.matrix.copy()
        else:
            self.matrix = []
        self.matrix.append(new_vector)
        self.line = line


class MatrixElement(Node):
    def __init__(self, id, index_x, index_y, line):
        self.id = id
        self.index_x = index_x
        self.index_y = index_y
        self.line = line


class Vector(Node):
    def __init__(self, new_elem, line, vector=None):
        self.vector = vector.vector.copy() if vector else []
        self.vector.append(new_elem)
        self.line = line


class VectorElement(Node):
    def __init__(self, id, index, line):
        self.id = id
        self.index = index
        self.line = line


class ID(Node):
    def __init__(self, id):
        self.id = id


class Assignable(Node):
    def __init__(self, id, index=None):
        self.id = id
        self.index = index


class String(Node):
    def __init__(self, string):
        self.string = string


class Instructions(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class IntNum(Node):
    def __init__(self, value):
        self.value = value


class Float(Node):
    def __init__(self, value):
        self.value = value


class Start(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class Printable(Node):
    def __init__(self, printables):
        self.printables = printables


class Error(Node):
    def __init__(self):
        pass
