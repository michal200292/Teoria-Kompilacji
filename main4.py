import sys
import ply.yacc as yacc
from src import scanner
from src.parser import parser
from src.TypeChecker import TypeChecker

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "tests/control_transfer.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = parser.parser
    # parser = yacc.yacc(module=parser)
    text = file.read()

    ast = parser.parse(text, lexer=scanner.lexer)
    # Below code shows how to use visitor
    typeChecker = TypeChecker()
    typeChecker.visit(ast)  # or alternatively ast.accept(typeChecker)
