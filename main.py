import sys
import scanner

# https://home.agh.edu.pl/~mkuta/tklab/
# pip3 freeze > requirements.txt

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    try:
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    lexer = scanner.lexer
    lexer.input(text)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break    # No more input
        print("%d: %s(%s)" %(tok.lineno, tok.type, tok.value))