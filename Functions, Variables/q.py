n = int(input())
if(n%2==1):
    print("Weird")
else:
    if(n in range(2,5)):
        print("Not Weird")
    elif(n in range(6,20)):
        print("Weird")
    else:
        print("Not Weird")
