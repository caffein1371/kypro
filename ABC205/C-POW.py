A,B,C =map(int,input().split())
if C%2==0:
    if abs(A)>abs(B):
        print ('>')
    elif abs(A)<abs(B):
        print ('<')
    elif abs(A)==abs(B):
        print ('=')
elif C%2==1:
    if A>B:
        print('>')
    elif A<B:
        print ('<')
    elif A==B:
        print ('=')