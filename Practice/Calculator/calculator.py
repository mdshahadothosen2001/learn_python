T=7
step1=input('Enter -> N for ON: ')
while(T>5):
    if('N' in step1):
        print("Enter Your Expression !")
        a=int(input())
        b=input()
        c=int(input())
        
        if('+' in b):
            a=a+c
            print(a)
        elif('-' in b):
            a=a-c
            print(a)
        elif('*' in b):
            a=a*c 
            print(a)
        elif('/' in b):
            a=a/c 
            print(a) 
        elif('%' in b):
            a=a%c
            print(a)
        else:
            print('Thank You, Your Expression is Wrong !')

    stepN=input('Enter -> F for OFF, A for Again: ')
    if('F' in stepN):
        break

       






