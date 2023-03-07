print("Kushar Ghop,Sonatola,Bogura,BD")
people={}
print(type(people))
while(True):
    print('1 Human','2 Set Data','3 See Data','4 Update Data','0 Exit')
    press=(input('Press: '))
    press=int(press)
    if(press==1):
        name=input('Enter Name: ')
        temp={name:[]}
        people.update(temp)
    elif(press==2):
        print('set details')
        name=input('Enter Name: ')
        family=input('Enter Number of Family Members: ')
        properties=input('Amount of Property: ')
        if(name in people)==True:
            temp=people[name]
            temp.append(family)
            temp.append(properties)
            temp.append('1KeY1')
        else:
            print('Your are registared but you did not set data' )            
    elif(press==3):
        print('see data')
        name=input('Enter Name: ')
        if(name in people)==True:
            key=people[name]
            if('1KeY1' in key)==True:
                temp=people[name]
                print('\n...........................')
                print('\n',name,'\nFamily Members: ',temp[0],'\nProperty: ',temp[1])
                print('...........................\n')
    elif(press==4):
        print('update data')
        name=input('Enter Name: ')
        family=input('Enter Number of Family Members: ')
        properties=input('Amount of Property: ')
        if(name in people)==True:
            key=people[name]
            if('1KeY1' in key)==True:        
                temp=people[name]
                temp[0]=family
                temp[1]=properties                         

    elif(press==0):
        break
print('\n......................................')
print('......................................')
print('\tThanks for connected !')
print('\tpowered by KushGhop')
print('\t@team')
print('......................................')
print('......................................\n')        