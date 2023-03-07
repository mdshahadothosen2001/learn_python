a=[1,2,3,4,5,6,7,8,9,11]
with open("data.txt","a") as fi:
    fi.write(str(a))
    fi.write('\n')
