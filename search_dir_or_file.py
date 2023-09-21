import os
import platform
search_folder_file = input("Enter the file name:")

for roots,dirs,files in os.walk("/home/muhammad/"):
    for i in files,dirs:
        if i == search_folder_file:
            print(os.path.join(roots,i))

 ---------- Output ---------------
 Enter the file name:ansible
 /home/muhammad/ansible
 /home/muhammad/ansible/ansible
