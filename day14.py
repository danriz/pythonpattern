for x in range(4):
    for h in range(3):
        for y in range(6):
            if y==1 or y==4 or (x==0 and y in [2,3] or (x==3 and y==0) or (x==3 and y==5)):
                print('*'.rjust(3),end='')
            else:
                print(' '.rjust(3),end='')
    print()
