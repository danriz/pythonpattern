
def array_printer(myrange):
    arr=[['-' for x in range (myrange)] for y in range (myrange)]

    mychar='A'
    k=myrange-1
    h=0
    for ii in range (myrange):
        for x in range (myrange):
            for y in range (myrange):
                if (x==k or y==h) and arr[x][y]=='-':
                    arr[x][y]=mychar
        h=h+1
        k=k-1
        mychar=chr(ord(mychar)+1)



    print('final result')
    for x in range (len(arr)):
        for y in range (len(arr[0])):
            print(arr[x][y].rjust(3),end='')
        print()

def array_printer2(hh):
    for i in range(hh):
        for j in range(hh):
            print(chr(65 + min(j, hh-1 - i)).rjust(3), end=' ')
        print()

    mylist=['A','B','C','D','E']
    k=1

def array_printer3(5):
    for x in range (len(mylist[:])):
        for y in range (len(mylist)):
            print(mylist[y]*k if y==len(mylist)-1 else mylist[y],end='' )
        mylist.pop()
        k=k+1
        print()

array_printer(10)
array_printer2(10)
array_printer3(5)
