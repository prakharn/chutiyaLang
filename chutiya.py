#########
# LEXER #
#########

# defining the Lexer class, initiating it and making it break down the input text into tokens.
class Lexer:    
    def __init__(self, inp):
        self.inp = inp
        self.i = 0
        self.tokenStack = self.tokenize()

    def tokenize(self):
        tokens=[]
        for rows in self.inp.split('\n'):
            for token in rows.split(' '):
                  if token == 'print':
                      tokens.append('print')
                  elif token == 'input':   # didn't have time to add inputs to parser so this is kinda useless
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
                      print("syntax err")                   
        return tokens
    def advance(self):
        if self.i < len(self.tokens):
            current_token = (self.tokens)[self.i]
            self.i+=1
            return(current_token)
        else:
            return None

##########
# PARSER #
##########

# defining the Parser class, taking the input tokens and assigning a proper response to the given tokens.
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
        while self.i<len(self.tokens):
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
