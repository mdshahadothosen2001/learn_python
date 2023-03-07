# f string
name='Md. Shahadot Hosen'
user=f"Hey,{name} welcome to our platform"
print(user)

# format
user="Hey,{} welcome to our platform".format(name)
print(user)

ID=20001
user="Hey,{} welcome to our platform,your id is {}".format(ID,name)
print(user)
# format index
user="Hey,{1} welcome to our platform,your id is {0}".format(ID,name)
print(user)