'''use below commands in REPL'''
#os module used to  interact with operating system to automate
import os
print(os.sep) #'\' is considered as path seperator
print(os.getcwd()) # current working path
os.chdir("C:\\PY\\scripting") #'\\' for windows users
print(os.listdir()) #can also list 'os.listdir(c\scripting)'
os.mkdir("folder_name") #create folder
os.makedirs("\scripting\x\y\z") #creates recursive folders
os.rmdir("path") #
os.removedirs("path")
os.rename("src","dst")
print(os.environ)
print(os.getuid()) # '>> dir(os)' to understand more
print(os.pid())#current shell process id