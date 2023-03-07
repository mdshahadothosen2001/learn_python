def BD():
    a=12
    def Bogura():
        #nonlocal a
        a=10
        print('Bogura',a)
    Bogura()
    print('BD',a)

BD()