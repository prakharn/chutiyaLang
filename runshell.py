import chutiya

while True:
    text = input("» chutiya » ")
    result, error = chutiya.run(text)
    
    if error:
        print(error.err_string())
    else:
        print (result)