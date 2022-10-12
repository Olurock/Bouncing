import os
path1 = 'C:/Mydir1'
#os.mkdir(path1)
# immediate folder
path2 = 'C:/Mydir2/practice'
#os.makedirs(path2)
# removing a dir

#os.remove()
print(os.listdir())
print(os.getcwd())
list = os.listdir()
for font1 in list:
    os.remove(font1)
