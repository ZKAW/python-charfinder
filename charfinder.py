while True:
    number = 0
    try:
        char = raw_input("Character or ASCII ID: ")
    except:
        char = input("Character or ASCII ID: ")
    try:
        print(str(chr(int(char)))+": "+char)
    except:
        for i in range(1,250):
            number+=1
            if chr(i) == char:
                print(str(number)+": "+chr(i))
