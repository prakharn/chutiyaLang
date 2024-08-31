##########
# TOKENS #
##########

# defining the type of tokens we will use in the code
integerNo = 'int'
floatNo = 'flt'
plus = 'plus'
minus = 'minus'
multiply = 'mult'
divide = 'div'
Lparen = 'Lpar'
Rparen = 'Rpar'

# defining the class token, initiating it and representing it
class Token():
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#########
# LEXER #
#########

# defining the Lexer class, initiating it and making it traverse through text.
# The lexer will go through are code and tokenize the text for the compiller to understand
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos += 1
        self.current_char = self.text[pos] if self.pos < len(self.text) else None
    
    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char == '+':
                tokens.append(plus)
                self.advance()
            elif self.current_char == '-':
                tokens.append(minus)
                self.advance()
            elif self.current_char == '*':
                tokens.append(multiply)
                self.advance()
            elif self.current_char == '/':
                tokens.append(divide)
                self.advance()
            elif self.current_char == '(':
                tokens.append(Lparen)
                self.advance()
            elif self.current_char == ')':
                tokens.append(Rparen)
                self.advance()
        return tokens
    
    def make_number(self):
        num_str = ''
        dot_count = 0
        

