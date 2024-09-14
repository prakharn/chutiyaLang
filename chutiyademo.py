# Token class
class Token:
    def __init__(self, val):
        self.value = val

#########
# LEXER #
#########

class Lexer:
    def __init__(self, inp):
        self.inp = inp
        self.i = 0
        self.tokens = self.tokenize()  # Changed tokenStack to tokens

    def tokenize(self):
        tokens = []
        for rows in self.inp.split('\n'):  # Changed from '/\n' to '\n' for line splitting
            for token in rows.split(' '):
                if token == 'print':
                    tokens.append('print')
                elif token == 'input':
                    tokens.append('input')
                elif token == '+':
                    tokens.append(['+', 'add'])
                elif token == '-':
                    tokens.append(['-', 'sub'])
                elif token == '*':
                    tokens.append(['*', 'mul'])
                elif token == '/':
                    tokens.append(['/', 'div'])
                elif token.isnumeric():
                    tokens.append(token)
                elif token == '':
                    pass
                elif token.isalpha():
                    tokens.append(token)
                else:
                    print("syntax error")
        return tokens

    def advance(self):
        if self.i < len(self.tokens):  # Fixed reference from self.tokenStack to self.tokens
            current_token = self.tokens[self.i]
            self.i += 1
            return current_token
        else:
            return None
##########
# PARSER #
##########

class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.i=0

    def advance(self):
        if self.i < len(self.tokens):
            current_token = (self.tokens)[self.i]
            self.i+=1
            return(current_token)
        else:
            return None

    def parsePrint(self):
        if self.tokens[self.i]=='print':
            self.advance()
            next_token = self.advance()
            print (next_token)
    #######
    # RUN #
    #######

def run(inp):
    lexer = Lexer(inp)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return tokens, parser
