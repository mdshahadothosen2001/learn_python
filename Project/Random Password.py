# Auto genarate password create

import random


lower_case="abcdefghijklmnopqrstuvwxyz"
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbol="!@#$%^&*()/?|}{:_+=<>~"

use=lower_case+upper_case+number+symbol

length=8
Password="".join(random.sample(use,length))
print("Password: ",Password)
