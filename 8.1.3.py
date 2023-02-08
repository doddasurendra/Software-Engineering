def happynumber(num):
    sum=0
    rem=0
    while(num>0):
        rem = num%10
        sum = sum+ (rem*rem)
        num=num//10
    return sum
num = int(input("enter a number:"))
if num<0:
 print ("enter  a postivive number")
result = num
while(result!=1 and result!=4):
     result = happynumber (result);
if (result ==1):
    print("true")
elif (result ==4):
    print("false")
