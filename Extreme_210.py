#!/usr/bin/env python3.

import paramiko
import time
import re

print('#########  Script started at: {}  #########'.format(time.strftime("%d-%m-%Y %H:%M:%S")))
date = time.strftime("%m-%d-%Y")


host = '10.1.1.1'
user = 'yyy'
port = 22
#key_path = '/home/yyy/.ssh/id_rsa'
pass_ssh = 'xxx'
ssh = paramiko.SSHClient()
# add server key to known
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(hostname=host, username=user, password=pass_ssh, port=port)    
    time.sleep(1)
except paramiko.ssh_exception.NoValidConnectionsError:
    logger.debug("Could not connect to host {}".format(host))
    print("Could not connect to host {}".format(host))
except Exception as e:
    print("Some error: %s" % e)
    raise SystemExit(2)


ssh.connect(hostname=host, username=user, password=pass_ssh, port=port)

print('  ssh connected  ')
channel = ssh.get_transport().open_session()
channel.get_pty()
channel.settimeout(50)
channel.invoke_shell()

while channel.recv_ready():
    channel.recv(1024)

###    Start to sends commands ###

channel.sendall("enable\n")
time.sleep(1)

channel.sendall("zzz\n")
time.sleep(1)

channel.sendall('copy nvram:startup-config tftp://10.1.1.1/Extreme-210/{}\n'.format(date))
time.sleep(0.5)
print('Name of Backup file is "{}"'.format(date))


channel.sendall("y\n")
time.sleep(5)


###    End of send commands ###

# For debug
#print(type(channel.recv(1024)))
#print('Channel buffer is :  {}'.format(channel.recv(1024))) ####

a = channel.recv(1024)
a = a.decode('utf-8')

#print('a is {}'.format(a)) ####

if (len(re.findall(r'y+', a))):
    print('*****  Success  ******')
else:
    print('*****  Something wrong!!!  *****')

channel.close()
ssh.close()

