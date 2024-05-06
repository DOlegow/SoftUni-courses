password = 'icecream::hot::summer'
index = '15'
length = '3'
print(int(index+length))
sub = password[int(index):int(index)+int(length)]
print(sub)
print(password)
print(password.replace(sub, '', 1))
