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
                      tokens.append('+')
                  elif token == '-':
                      tokens.append('-')
                  elif token == '*':
                      tokens.append('*')
                  elif token == '/':
                      tokens.append('/')
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
            current_token = self.tokens[self.i]
            if self.i+1 < len(self.tokens):
                self.i+=1
            else:
                return(None)
            next_token = self.tokens[self.i]
            return(next_token)
        else:
            return None

    def parsePrint(self):
        while self.i<len(self.tokens):
            if self.tokens[self.i]=='print':
                next_token = self.advance()
                print(next_token)
                self.advance()
            else:
                break
    def parseMath(self):
        while self.i<len(self.tokens):
            if self.tokens[self.i].isnumeric():
                current_token = self.tokens[self.i]
                next_token = self.advance()
                if next_token == '+':
                    next_token = self.advance()
                    sum = int(current_token) + int(next_token)
                    print(sum)
                    self.advance()
                elif next_token == '-':
                    next_token = self.advance()
                    sub = int(current_token) - int(next_token)
                    print(sub)
                    self.advance()
                elif next_token == '/':
                    next_token = self.advance()
                    div = int(current_token) / int(next_token)
                    print(div)
                    self.advance()
                elif next_token == '*':
                    next_token = self.advance()
                    prod = int(current_token) * int(next_token)
                    print(prod)
                    self.advance()
                elif self.advance()==None:
                    break

            else:
                break
                


#######
# RUN #
#######

def run(inp):
    lexer = Lexer(inp)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return tokens, parser
