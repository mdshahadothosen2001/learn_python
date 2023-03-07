from functools import reduce

sum= lambda a,b:a+b
a=[1,2,3,4,5]
values=reduce(sum,a)
print(values)
