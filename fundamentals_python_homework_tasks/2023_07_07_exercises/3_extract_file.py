txt = input().split("\\")
file_extension = txt[-1]
file_list = file_extension.split('.')
print(f'File name: {file_list[0]}')
print(f'File extension: {file_list[1]}')
