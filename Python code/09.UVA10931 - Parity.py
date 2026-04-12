while 1:
    try:
        name = int(input())
    except EOFError:
        break
    if name == 0:
        break
    name = bin(name)
    print("The parity of", name[2:], "is", name.count("1"), "(mod 2).")