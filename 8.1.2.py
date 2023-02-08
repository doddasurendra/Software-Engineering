n= int(input("enter the terms"))
empty =[]
for i in range (n):
    x= int(input())
    empty.append(x)
    print(empty)
def sumsquare(r):
    odd=0
    even=0
    for i in r:
        if i%2==0:
            even=even+i**2
        else:
            odd=odd+i**2
    r=[odd,even]
    return(r)
print(sumsquare(empty))
