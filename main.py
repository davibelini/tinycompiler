import sys
from tinycompiler.token import TokenType

from tinycompiler import lexer

def main():
    #src = (open(sys.argv[1]).read())
    debug_src = '''"hello world"//sadfsadfsadfasdf\n+- */ >>= = !='''
    l = lexer.Lexer(debug_src)

    token = l.get_token()
    while token.kind != TokenType.EOF:
        print(token.kind, token.text)
        token = l.get_token()
main()