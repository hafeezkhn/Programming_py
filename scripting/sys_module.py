
'''use below commands in REPL'''
#sys modules provide func and var used to manuplate different parts of "python runtime env"
# >> dir(sys)  -> gives (list of) operations,variables,functions which are there
# >> help(sys) -> document (details of) 

import sys

print(sys.version)
print(sys.modules)#shows all modules which are imported which includes builtins
print(sys.path) #libraries and modules path(environment variable for python)
print("\n\n\n")
print(sys.argv) #command line arguments (all elements in string)
print(sys.argv[0]) #index zero is script name
print(len(sys.argv)) #no. of arguments

sys.exit() #stops execution of script
