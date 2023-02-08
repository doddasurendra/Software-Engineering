def sai (str1,str2):
    if len(str1)!=len(str2):
         return False
    for i in range (len(str1)):
	    count=0
    if str1.count(str1[i])!= str2.count(str2[i]):
	    return False
    return True  
print(sai("egg","add"))
print(sai("foo","bar"))
print(sai("paper","title"))
print(sai("fry","sky"))
print(sai("apples","apple"))

