field = [["-" for i in range(3)] for i in range(3)]
for i in range(4):
    if i:
        print(f"{i-1} ", end = "")
    else:
        print("  0 1 2")

    for j in range(4):
        if i:
            print(f"{field[i-1][j-1]} ", end = "")
        else:
            print(f"{j} ", end = "")
    print()