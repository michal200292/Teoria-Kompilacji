class Node(object):

    def print_node(self, indent):
        print("|   " * indent, end="")


class Instruction(Node):
    def __init__(self, instruction):
        self.instruction = instruction


class Printable(Node):

    def __init__(self, expression):
        self.expression = expression


class Assignable(Node):

    def __init__(self, value):
        self.value = value


class String(Node):

    def __init__(self, value):
        self.value = value


class WhileInstruction(Node):

    def __init__(self, expression, instruction):
        self.expression = expression
        self.instruction = instruction


class ForInstruction(Node):

    def __init__(self, variable, expression, instruction, exp_range):
        self.variable = variable
        self.expression = expression
        self.instruction = instruction
        self.exp_range = exp_range


class IfInstruction(Node):

    def __init__(self, expression, instruction, else_instruction):
        self.expression = expression
        self.instruction = instruction
        self.else_instruction = else_instruction


class PrintInstruction(Node):

    def __init__(self, printable):
        self.printable = printable


class ReturnInstruction(Node):

    def __init__(self, expression):
        self.expression = expression


class AssignInstruction(Node):

    def __init__(self, assignable, instruction, expression):
        self.assignable = assignable
        self.instruction = instruction
        self.expression = expression


class Transpose(Node):

    def __init__(self, matrix):
        self.matrix = matrix


class CreateMatrix(Node):

    def __init__(self, matrix_type, size):
        self.matrix_type = matrix_type
        self.size = size


class Continue(Node):
    def __init__(self):
        pass


class Break(Node):
    def __init__(self):
        pass


class Return(Node):
    def __init__(self, value):
        self.value = value


class ID(Node):

    def __init__(self, value):
        self.value = value


class IntNum(Node):
    def __init__(self, value):
        self.value = value


class FloatNum(Node):

    def __init__(self, value):
        self.value = value


class Variable(Node):
    def __init__(self, name):
        self.name = name


class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
