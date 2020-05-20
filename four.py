def find(x,y):
    temp=0
    for i in range(1,max(x,y)+1):
        if (x % i == y % i == 0):
            temp+=1
    print(temp)
    return None
if __name__=="__main__":
    x=int(input())
    y=int(input())
    find(x,y)
