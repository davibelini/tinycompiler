import sys

from tinycompiler import lexer

def main():
    #l = Lexer(open(sys.argv[1]).read())
    l = lexer.Lexer("++++++++++++")
    while l.peek() != "\0":
        print(l.get_token().kind)
main()