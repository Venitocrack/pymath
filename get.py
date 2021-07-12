import inspect
import os,re
os_file = inspect.getfile(os)
print(re.sub("os.py","",os_file))
