def sq(n):
    return n*n

#method 1 # normally
a=[1,2,4]
a1=[]
for item in a:
    a1.append(sq(item))

print(a1)


print(list(map(sq,a)))