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
        return self.source[self.cur_pos]

    def abort(self, message):
        pass

    def skip_whitespace(self):
        pass

    def skip_comment(self):
        pass

    def get_token(self):
        token = ''

        if self.cur_char == '+':
            token = Token(self.cur_char, TokenType.PLUS)
        
        elif self.cur_char == '-':
            token = Token(self.cur_char, TokenType.MINUS)
            
        elif self.cur_char == '*':
            token = Token(self.cur_char, TokenType.ASTERISK)
        
        elif self.cur_char == '/':
            token = Token(self.cur_char, TokenType.SLASH)

        elif self.cur_char == '\n':
            token = Token(self.cur_char, TokenType.NEWLINE)

        elif self.cur_char == '\0':
            token = Token(self.cur_char, TokenType.EOF)

        else:
            pass

        self.advance()
        return token