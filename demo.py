inp = input("chut ")
tokens=[]
for rows in inp.split('\n'):
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
                      print (token)
                  else:
                      print("syntax err") 

print(tokens)