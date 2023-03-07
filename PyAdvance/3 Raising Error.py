def up(n):
    try:
        return int(n)*10
    except:
        raise ValueError("Invalid value")

a=up('g89')
print(a)

#b=up('dfg34')
#print(b)