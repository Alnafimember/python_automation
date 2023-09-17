import os
print("My path of dir in which am working ", os.getcwd())
print("My current uid is :" , os.getuid())
print("My current group id is :" , os.getgid())
print("My current process id is :" ,os.getpid())
print(os.walk(os.listdir()))
print(os.walk(os.getcwd()))
