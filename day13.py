spaces=[' ']*(5-1)
my_char='A'
my_num=1

for x in range(5):
    for s in spaces:
        print(s.rjust(3),end='')
    if(len(spaces)>0):
        spaces.pop()
    my_char = chr(ord('A') + x)
    my_num= 1+x
    for stringprint in range (x+1):
        print(my_char.rjust(3),end='')

        my_char = chr(ord(my_char) + 1)

    for numberprint in range (x+1):
        print(str(my_num).rjust(3), end='')
        my_num = my_num + 1

    print()
