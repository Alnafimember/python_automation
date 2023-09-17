import os
T_memory=os.popen ( " free -g | grep -iw 'Mem'|awk '{print $2}' ").read()
print("Total Memory : ", T_memory)
s_memory=os.popen ( " free -g | grep -iw 'Swap' |awk '{print $2}'").read()
print("Swap Memory :", s_memory)
u_memory=os.popen ( " free -g | grep -iw 'Mem' |awk '{print $3}' ").read()
print("Used Memory:", u_memory)
