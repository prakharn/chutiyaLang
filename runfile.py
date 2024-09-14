import sys, chutiya

with open(sys.argv[1], 'rt') as f:
    file = f.read()

tokens, parser = chutiya.run(file)
parser.parsePrint()