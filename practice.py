def set_diff(a,b):
    x = []
    for i in a:
        if i not in b:
            x.append(i)
    print(x)

#Making changes to the file in cloned repo  
# Making changes to the repo that pulled 
## New architect involved to make changes , so new branch created without disturbing others work

m = int(input("ENter"))
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:m]
n = int(input("ENter"))
b = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
set_diff(a,b)