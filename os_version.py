import os
my_os_version= " cat /etc/os-release |grep -iw 'Version'|awk -F '=' '{print $2}' |tr '\n\' ' ' "
os_version=os.popen(my_os_version).read()
print(os_version)
