while(True):
    print('Press any key for Continue, write stop ')
    x=input()
    if('stop' in x):
        break
    
    try:
        print('Enter any integer')
        y=int(input())
        if(y>0):
            print('You pressed Positive Number')
        elif(y<0):
            print('You pressed Negative Number')

    except Exception as e:
        print("Error ",e)
print('Thanks for Playing this Game!') 


