# Working With Files

# 1) write
#create and write 
with open('user_info.txt', 'w') as file:
  file.write('this is my first txt file using python')

# appending in existing file 
with open('user_info.txt', 'w') as file:
  file.write('second line \n')
  
  # 2) read 
with open('user_info.txt' , 'r') as file:
  # content = file.read()
    content = file.readlines()

for line in content:
  print(line.rstrip()) #to remove extra line (.rstrip())


