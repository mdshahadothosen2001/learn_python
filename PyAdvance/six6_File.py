def sona(name):
    print('Hey sweet heart,',name)

# if _ _ name_ _ =="_ _ main_ _"
# means if we run this file from this file then work it
# but if import this file from anywhere then not work these statement only work sona() fun
#print( __name__)
if __name__=="__main__":
    print("Enter your pls")
    name=input()
    sona(name)