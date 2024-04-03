database=["croaks","eat files","shrimps","sings"]
knowbase=["frog","canary"]
color=["green","yellow"]
def display():
    print("\n x is \n 1. frog \n2.canary",end='')
    print("\n select one",end='')
def main():
    print("*  backword  *",end='')
    display()
    x=int(input())
    print("\n",end='')
    if x==1:
        print("chance of eating files",end='')
    elif x==2:
        print("chance of shrimping",end='')
    else:
        print("\n  invalid op   ",end='')
    if x>=1 and x<=2:
        print("\n x is",end='')
        print(knowbase[x-1],end='')
        print("\n color is 1.green 2.yellow")
        k=int(input())
        if k==1 and x==1:
            print("yes it is",end='')
            print(database[0])
            print("and color is",end='')
            print(color[0],end='')            
        elif k==2 and x==2:
            print("yes it is",end='')
            print(database[1])            
            print(" color and will",end='')
            print(color[1],end='')
        else:
            print("\n  invalid  db",end='')
if __name__=="__main__":
    main()
