if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

    p = 0
    p2 = 0
    p3 = 0

    output = '[';
    is_added = False

    for i1 in range(0, x + 1):
        for i2 in range(0, y + 1):
            for i3 in range(0, z + 1):
                if(i1 + i2 + i3 != n):
                    is_added = True
                    output += '[' + str(i1) + ', ' + str(i2) + ', ' + str(i3) + '], '
    if(is_added):
        output = output[:-2]
    output += ']'
    print(output)
