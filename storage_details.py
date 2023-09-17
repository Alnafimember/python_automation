import os
r_name=os.popen("df -h|grep -iw '/dev/sda5' |awk '{print $6}' ").read()
print("Root Directories name is :", r_name)
r_total_size=os.popen("df -h|grep -iw '/dev/sda5' |awk '{print $2}'").read()
print("Root Directories total size is : ", r_total_size)
r_used_size=os.popen("df -h|grep -iw '/dev/sda5' |awk '{print $3}'").read()
print("Root Directories used size is :", r_used_size)
