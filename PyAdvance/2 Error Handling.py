try:
    print('Enter any integer')
    a=int(input())
    b=1/a
    print(b)

except ValueError as e:
    print("Please enter valid value ")
except ZeroDivisionError as e:
    print("Make sure can't divide by Zero")    
print('Thanks for Playing this Game!') 


