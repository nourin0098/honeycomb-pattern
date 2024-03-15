def draw_honeycomb(a, b):
    print("Inputs :-", a, " ", b)
    for i in range(a):
        a_1 = {1: "", 2: "", 3: ""}
        for j in range(b):
            if i == 0:
                a_1[1] += " __   " if j % 2 == 0 else ""
            if j % 2 == 0:
                a_1[2] += "/  \\" if j != b - 1 else "/  \\"
                a_1[3] += "\\__/" if j != b - 1 else "\\__/"
            else:
                a_1[2] += "__" if j != b - 1 else "__"
                a_1[3] += "  " if j != b - 1 else "  "
        if a_1[1]:
            print(a_1[1])
        print(a_1[2])
        print(a_1[3])
    print("")

draw_honeycomb(4, 7)
draw_honeycomb(3, 5)
