import os
import platform
if platform.system() == "Linux":
    for i in os.listdir("/home/muhammad/ansible/"):
        if i.endswith(".txt"):
            print(i)
elif platform.system() == "Windows":
    for i in os.listdir("C:/User/"):
        if i.endswith(".txt"):
            print(i)
