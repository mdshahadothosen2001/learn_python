try:
    x=int(input())
    y=1/x
    print(y)

except Exception as e:
    print("Please enter value again")

else:
    print('Successfully Done!')        