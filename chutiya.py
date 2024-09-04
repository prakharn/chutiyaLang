##########
# TOKENS #
##########

# defining the type of tokens we will use in the code
Tint = 'int'
Tfloat = 'flt'
Tplus = 'plus'
Tminus = 'minus'
Tmult = 'mult'
Tdiv = 'div'
TLparen = 'Lpar'
TRparen = 'Rpar'

# defining the class token, initiating it and representing it
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#############
# CONSTANTS #
#############

DIGITS='0123456789'

##########
# ERRORS #
##########

class Error:
    def __init__(self, err_name, details):
        self.err_name = err_name
        self.details = details
    def err_string(self):
        result = f'{self.err_name}:{self.details}'
        return result

class illegalChar(Error):
    def __init__(self, details):
        super().__init__(self, details)        

############
# POSITION #
############

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
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
    
    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Tplus)
                self.advance()
            elif self.current_char == '-':
                tokens.append(Tminus)
                self.advance()
            elif self.current_char == '*':
                tokens.append(Tmult)
                self.advance()
            elif self.current_char == '/':
                tokens.append(Tdiv)
                self.advance()
            elif self.current_char == '(':
                tokens.append(TLparen)
                self.advance()
            elif self.current_char == ')':
                tokens.append(TRparen)
                self.advance()
            else:
                char = self.current_char
                self.advance()
                return [], illegalChar(char+" chutiya, ye illegal hai")
        return tokens, None
    
    def make_number(self):
        num_str = ''
        dot_count = 0
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
        if dot_count == 0:
            return Token(Tint, int(num_str))
        else:
            return Token(Tfloat, float(num_str))

#########
# NODES #
#########

class numberNode:
    def __init__(self, token):
        self.token = token
    def __repr__(self):
        return f'{self.token}'

class binaryOperatorNode:
    def __init__(self, lnode, opr, rnode):
        self.lnode = lnode
        self.opr = opr
        self.rnode = rnode
    def __repr__(self):
        return f'{self.lnode, self.opr, self.rnode}'

##########
# PARSER #
##########



#######
# RUN #
#######

def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()
    return tokens, error


