from __future__ import print_function
import src.AST as AST
# import graphviz


def addToClass(cls):
    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator


@addToClass(AST.Node)
def printTree(self, indent=0):
    raise Exception("printTree not defined in class " + self.__class__.__name__)


@addToClass(AST.BinaryExpr)
def printTree(self, indent=0):
    self.print_tab(indent)
    print(self.op)
    self.left.printTree(indent + 1)
    self.right.printTree(indent + 1)


@addToClass(AST.AssignOperation)
def printTree(self, indent=0):
    self.print_tab(indent)
    print(self.op)
    self.left.printTree(indent + 1)
    self.expression.printTree(indent + 1)


@addToClass(AST.IfCondition)
def printTree(self, indent=0):
    self.print_tab(indent)
    print("IF")
    self.cond.printTree(indent + 1)
    self.if_body.printTree(indent + 1)
    if self.else_body is not None:
        self.print_tab(indent)
        print("ELSE")
        self.else_body.printTree(indent + 1)


@addToClass(AST.While)
def printTree(self, indent=0):
    self.print_tab(indent)
    print("WHILE")
    self.cond.printTree(indent + 1)
    self.body.printTree(indent + 1)


@addToClass(AST.For)
def printTree(self, indent=0):
    self.print_tab(indent)
    print("FOR")
    self.begin.printTree(indent + 1)
    self.end.printTree(indent + 1)
    self.body.printTree(indent + 1)


@addToClass(AST.Break)
def printTree(self, indent=0):
    self.print_tab(indent)
    print("BREAK")


@addToClass(AST.Continue)
def printTree(self, indent=0):
    self.print_tab(indent)
    print("CONTINUE")


@addToClass(AST.Return)
def printTree(self, indent=0):
    self.print_tab(indent)
    print("RETURN")
    if self.expr is not None:
        self.expr.printTree(indent+1)


@addToClass(AST.Print)
def printTree(self, indent=0):
    self.print_tab(indent)
    print("PRINT")
    for expr in self.exprs:
        expr.printTree(indent + 1)


@addToClass(AST.Transpose)
def printTree(self, indent=0):
    self.print_tab(indent)
    print("TRANSPOSE")
    self.arg.printTree(indent + 1)


@addToClass(AST.MatrixFunction)
def printTree(self, indent=0):
    self.print_tab(indent)
    print(self.function)
    self.arg.printTree(indent + 1)


@addToClass(AST.Matrix)
def printTree(self, indent=0):
    self.print_tab(indent)
    print("VECTOR")
    for row in self.matrix:
        self.print_tab(indent + 1)
        print("VECTOR")
        for expr in row:
            self.print_tab(indent + 2)
            print(expr)


@addToClass(AST.Uminus)
def printTree(self, indent=0):
    self.print_tab(indent)
    print("-")
    self.expression.printTree(indent + 1)


@addToClass(AST.ID)
def printTree(self, indent=0):
    self.print_tab(indent)
    print(self.id)


@addToClass(AST.Assignable)
def printTree(self, indent=0):
    self.id.printTree(indent)
    if self.index is not None:
        self.print_tab(indent)
        print("REF")
        for expr in self.index:
            self.print_tab(indent + 1)
            print(expr)


@addToClass(AST.String)
def printTree(self, indent=0):
    self.print_tab(indent)
    print("STRING")
    self.print_tab(indent + 1)
    print(self.string)


@addToClass(AST.Instructions)
def printTree(self, indent=0):
    for instruction in self.instructions:
        instruction.printTree(indent)


@addToClass(AST.IntNum)
def printTree(self, indent=0):
    self.print_tab(indent)
    print(self.value)


@addToClass(AST.Float)
def printTree(self, indent=0):
    self.print_tab(indent)
    print(self.value)


@addToClass(AST.Instructions)
def printTree(self, indent=0):
    for instruction in self.instructions:
        instruction.printTree(0)


@addToClass(AST.Error)
def printTree(self, indent=0):
    pass

