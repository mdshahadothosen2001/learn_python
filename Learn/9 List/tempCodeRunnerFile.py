
b=['Md','Shahadot','Hosen',['Competitive','Programming','Algorithms','Number Theory','Graph','Math'], 'Software','Engineer']    

for i in b:
    if type(i) is list:
        for j in i:
            print(j)