database=["croaks","eat files","shrimps","sings"]
knowbase=["frog","canary","green","yellow"]
def display():
    print("\n x is \n 1.. croaks \n2.eat files \n3.shrimps \n4 sings",end='')
    print("\n select one",end='')
def main():
    print("*  farward  *",end='')
    display()
    x=int(input())
    print("\n",end='')
    if x==1 or x==4:
        print("chance of frog",end='')
    elif x==3 or x==4:
        print("chance of canary",end='')
    else:
        print("\n  invalid op   ",end='')
    if x>=1 and x<=4:
        print("\n x is",end='')
        print(database[x-1],end='')
        print("\n color is 1.green 2.yellow",end='')
        print("\n select op",end='')
        k=int(input())
        if k==1 and (x==1 or x==2):
            print("yes it is",end='')
            print(knowbase[0],end='')
            print("and color is",end='')
            print(knowbase[2],end='')
        elif k==2 and (x==3 or x==4):
            print("yes it is",end='')
            print(knowbase[1],end='')
            print("and color is",end='')
            print(knowbase[3],end='')
        else:
            print("\n  invalid  db",end='')
if __name__=="__main__":
    main()
