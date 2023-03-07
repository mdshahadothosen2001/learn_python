def greater(n):
    if n>10:
        return True
    else:
        return False

a=[1,2,3,4,5,56,7,8,19]
print(list(filter(greater,a)))

# use lambda
g=lambda num:num>10
b=[1,2,3,4,5,56,7,8,19]
print(list(filter(g,b)))
