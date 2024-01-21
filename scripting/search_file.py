''' 
>> python .\scripting\search_file.py           
enter file name to search test001.py
/workspace\git_repo\Programming_py\pyui\ex01\test001.py
/workspace\git_repo\Programming_py\pyui\ex02\test001.py
'''

import os
req_file = input("enter file name to search ")
for r,d,f in os.walk("/"):
    for each_file in f:
        if each_file == req_file:
            print(os.path.join(r,each_file))

    