from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    counter = 1
    output = 0

    while(True):
        if(n == 0):
            break
        output += n * (counter)

        counter = counter * 10

        if(n > 9):
            counter = counter * 10
        if(n > 99):
            counter = counter * 10

        n = n - 1

    print(output)
