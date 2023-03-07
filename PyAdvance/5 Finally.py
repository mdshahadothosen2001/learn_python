try:
    x=int(input('Enter: '))
    y=1/x
    print(y)
except Exception as Er:
    print('Error is ',Er)
    exit()

finally:
    print('Success!')


print('It working when found error becase use exit() in except part  but finall part must be executed always')

## Without finally part: 
# try:
#    x=int(input('Enter: '))
#    y=1/x
#    print(y)
#except Exception as Er:
#    print('Error is ',Er)


#print('Success!')   