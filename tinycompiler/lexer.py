import sys

from tinycompiler.token import TokenType, Token
from token import *

class Lexer:
    def __init__(self, input):
        self.source = input + '\n'
        self.cur_pos = -1
        self.cur_char = ''
        self.advance()

    def advance(self):
        self.cur_pos += 1
        if self.cur_pos >= len(self.source):
            self.cur_char = "\0"
        else:
            self.cur_char = self.source[self.cur_pos]

    def peek(self):
        if self.cur_pos + 1 >= len(self.source):
            return "\0"
        return self.source[self.cur_pos + 1]

    def abort(self, message):
        sys.exit(f"{message}")

    def skip_whitespace(self):
        while self.cur_char in ' \t\r':
            self.advance()

    def skip_comment(self):
        pass

    def get_token(self):
        self.skip_whitespace()
        token = ''

        if self.cur_char == '+':
            token = Token(self.cur_char, TokenType.PLUS)
        
        elif self.cur_char == '-':
            token = Token(self.cur_char, TokenType.MINUS)
            
        elif self.cur_char == '*':
            token = Token(self.cur_char, TokenType.ASTERISK)
        
        elif self.cur_char == '/':
            token = Token(self.cur_char, TokenType.SLASH)

        elif self.cur_char == '=':
            if self.peek() == '=':
                c = self.cur_char
                self.advance()
                token = Token(c + self.cur_char, TokenType.EQEQ)
            else:
                token = Token(self.cur_char, TokenType.EQ)

        elif self.cur_char == '>':
            if self.peek() == '=':
                c = self.cur_char
                self.advance()
                token = Token(c + self.cur_char, TokenType.GTEQ)
            else:
                token = Token(self.cur_char, TokenType.GT)

        elif self.cur_char == '<':
            if self.peek() == '=':
                c = self.cur_char
                self.advance()
                token = Token(c + self.cur_char, TokenType.LTEQ)
            else:
                token = Token(self.cur_char, TokenType.LT)

        elif self.cur_char == '!':
            if self.peek() == '=':
                c = self.cur_char
                self.advance()
                token = Token(c + self.cur_char, TokenType.NOTEQ)
            else:
                self.abort(f"expected '!=' got '!{self.cur_char}'")

        elif self.cur_char == '\n':
            token = Token(self.cur_char, TokenType.NEWLINE)

        elif self.cur_char == '\0':
            token = Token(self.cur_char, TokenType.EOF)

        else:
            pass

        self.advance()
        return token