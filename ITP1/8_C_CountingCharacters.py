

count = [0] * 26
while True:
    try:
      n = input()
    except:
      break
    for i in range(len(n)):
        if n[i]=='a' or n[i]=='A':
            count[0]+=1
        elif n[i]=='b' or n[i]=='B':
            count[1]+=1
        elif n[i]=='c' or n[i]=='C':
            count[2]+=1
        elif n[i]=='d'or n[i]=='D':
            count[3]+=1
        elif n[i]=='e'or n[i]=='E':
            count[4]+=1
        elif n[i]=='f'or n[i]=='F':
            count[5]+=1
        elif n[i]=='g'or n[i]=='G':
            count[6]+=1
        elif n[i]=='h'or n[i]=='H':
            count[7]+=1
        elif n[i]=='i'or n[i]=='I':
            count[8]+=1
        elif n[i]=='j'or n[i]=='J':
            count[9]+=1
        elif n[i]=='k'or n[i]=='K':
            count[10]+=1
        elif n[i]=='l'or n[i]=='L':
            count[11]+=1
        elif n[i]=='m'or n[i]=='M':
            count[12]+=1
        elif n[i]=='n'or n[i]=='N':
            count[13]+=1
        elif n[i]=='o'or n[i]=='O':
            count[14]+=1
        elif n[i]=='p'or n[i]=='P':
            count[15]+=1
        elif n[i]=='q'or n[i]=='Q':
            count[16]+=1
        elif n[i]=='r'or n[i]=='R':
            count[17]+=1
        elif n[i]=='s'or n[i]=='S':
            count[18]+=1
        elif n[i]=='t'or n[i]=='T':
            count[19]+=1
        elif n[i]=='u'or n[i]=='U':
            count[20]+=1
        elif n[i]=='v'or n[i]=='V':
            count[21]+=1
        elif n[i]=='w'or n[i]=='W':
            count[22]+=1
        elif n[i]=='x'or n[i]=='X':
            count[23]+=1
        elif n[i]=='y'or n[i]=='Y':
            count[24]+=1
        elif n[i]=='z'or n[i]=='Z':
            count[25]+=1


print ('a : {}'.format(count[0]))
print ('b : {}'.format(count[1]))
print ('c : {}'.format(count[2]))
print ('d : {}'.format(count[3]))
print ('e : {}'.format(count[4]))
print ('f : {}'.format(count[5]))
print ('g : {}'.format(count[6]))
print ('h : {}'.format(count[7]))
print ('i : {}'.format(count[8]))
print ('j : {}'.format(count[9]))
print ('k : {}'.format(count[10]))
print ('l : {}'.format(count[11]))
print ('m : {}'.format(count[12]))
print ('n : {}'.format(count[13]))
print ('o : {}'.format(count[14]))
print ('p : {}'.format(count[15]))
print ('q : {}'.format(count[16]))
print ('r : {}'.format(count[17]))
print ('s : {}'.format(count[18]))
print ('t : {}'.format(count[19]))
print ('u : {}'.format(count[20]))
print ('v : {}'.format(count[21]))
print ('w : {}'.format(count[22]))
print ('x : {}'.format(count[23]))
print ('y : {}'.format(count[24]))
print ('z : {}'.format(count[25]))
