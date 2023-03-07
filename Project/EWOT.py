# Employee's working over Times
users={}

while(True):
    print("\n......................","| 1 append           |","| 2 day hour         |","| 3 see working hour |","| 0 exit             |","|....................|",sep='\n')
    PASS=int(input("Pass: "))
    if(PASS==1):
        name=input("Enter Employee Name: ")
        user={name:[]}
        users.update(user)
    elif(PASS==2):
        name=input("Enter name: ")
        hour=int(input("Enter today's working hour: "))
        temp=users[name]
        temp.append(hour)    
    elif(PASS==3):
        name=input('Enter your name: ')
        temp=users[name]
        temp=sum(temp)
        print('\n\n',name,'congratulations! your working hour is : ',temp,'\n\n')
    elif(PASS==0):
        break
    else:
        print('try again')

print(users)
   