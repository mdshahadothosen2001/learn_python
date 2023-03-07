a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#b=[]
# for i in range(a): 
#     b.append(item)
# similar to it
b=[i for i in a]
# also use at for loop if a[i]%2==0:
#     b.append(item)
# simply similar it
c=[i for i in a if i%2==0]

# we can use also  at dict,set,tuple

print(a,b,c,sep='\n')