a=2
def fun():
    a=5
    print(a,'here fun')

fun()
print(a,'here main')    



b=2
def fun():
    global b
    b=5
    print(b,'here fun')

fun()
print(b,'here main') 




def fun():
    c=9
    
    def inFun():
        nonlocal c
        c=1
        print(c,'inner fun')
    inFun()
    print(c,'outer fun')

fun()
