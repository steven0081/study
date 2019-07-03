import  os

current_dir = os.getcwd()
file_list = os.listdir(current_dir)
print(file_list)
print(current_dir)
file=open(current_dir+'\\' + 'lesson1.py', 'r', encoding='UTF-8')
file_content = file.readlines()
print(file_content)

