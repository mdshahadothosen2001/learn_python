try:
    while(True):
        x=int(input("Press any key: "))
        if (x==0):
            break
        elif (x>10):
            print('Greater than 10')
        elif (x<10):
            print('Less than 10')    

except Exception as error:
    print('Error is : ',error)
    