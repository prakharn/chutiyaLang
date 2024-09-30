import chutiya

while True:
    inp = input("» chutiya » ")
    tokens, parser = chutiya.run(inp)
    parser.parsePrint()
    parser.parseMath()