while True:
    number = 0
    try:
        char = raw_input("Caractere ou code ASCII: ")
    except:
        char = input("Caractere ou code ASCII: ")
    try:
        print(str(chr(int(char)))+": "+char)
    except:
        for i in range(1,250):
            number+=1
            if chr(i) == char:
                print(str(number)+": "+chr(i))
