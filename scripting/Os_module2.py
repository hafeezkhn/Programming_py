'''use below commands in REPL'''
# os sub-modules used to  interact with operating system to automate

import os

#os.path  
print(os.path.sep)
print(os.path.basename("path"))
print(os.path.dirname("path"))
print(os.path.join(path1,path2))# same as "print(path1+'\'+path2)" ;path1="\home"; path2="scripting"
print(os.path.split('path'))
print(os.path.exists('path'))
print(os.path.isdir('path')) # os.path.isfile(path)

#os.system -> uses os commands
print(os.system("cls")) # os.system("any linux/windows terminal commands")
var = os.system("ls") # print(var)

#platform
import platform
print(platform.system()=="Windows")

#tree type 
print(list(os.walk('path'))) #taple value  recursive files and folders
for r,d,f in os.walk('path',topdown=False):#r = root, d=directory, f = file
    print(r,f)


