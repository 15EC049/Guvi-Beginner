a=int(input())
    temp=a
    su=0
    while(temp>0):
        r=temp%10
        su+=r**3
        temp//=10
    if(a==su):
        print("yes")
    else:
        print("no")

        
