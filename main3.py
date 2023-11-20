import sys
from src import scanner
from src.parser import parser
import src.TreePrinter


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "tests/example3.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    parser = parser.parser
    text = file.read()
    ast = parser.parse(text, lexer=scanner.lexer)
    ast.printTree()
