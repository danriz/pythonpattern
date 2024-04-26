h=1
for x in range (5):
    for y in range (5):
        if (x+y)%2==0:
            print('*'.rjust(3),end='')
        else:
            print(str(h).rjust(3),end='')
            h=h+1
    print()
