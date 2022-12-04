N = int(input())
temp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ans =[]
#print (28%702)
while N!=0:
    N-=1
    M = N%26
    ans.append(temp[M])
    N = N//26
    #print (N)

    
print ("".join(ans[::-1]))