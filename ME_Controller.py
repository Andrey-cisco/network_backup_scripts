#!/usr/bin/env python3.6

import paramiko
import time
import re

print('#########  Script started at: {}  #########'.format(time.strftime("%d-%m-%Y %H:%M:%S")))
date = time.strftime("%m-%d-%Y")


host = '10.2.1.1'
user = 'username'
port = 22
passphrase_ssh = 'xxx'
ssh = paramiko.SSHClient()
# add server key to known
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(hostname=host, username=user, password=passphrase_ssh, port=port)   
    time.sleep(1)
except paramiko.ssh_exception.NoValidConnectionsError:
    logger.debug("Could not connect to host {}".format(host))
    print("Could not connect to host {}".format(host))
except Exception as e:
    print("Some error: %s" % e)
    raise SystemExit(2)


time.sleep(1)
ssh.connect(hostname=host, username=user, port=port, password=passphrase_ssh)

time.sleep(1)
#print('  ssh connected  ')
channel = ssh.get_transport().open_session()
channel.get_pty()
channel.settimeout(50)
channel.invoke_shell()

time.sleep(1)
while channel.recv_ready():
    channel.recv(1024)

time.sleep(1)

# print(type(channel.recv(1024)))

###    Start to sends commands ###

channel.sendall("username\n")
time.sleep(1)

channel.sendall("pass\n")
time.sleep(1)

channel.sendall('transfer upload filename {}\n'.format(date))
channel.sendall("transfer upload path ME/\n")
channel.sendall("transfer upload mode tftp \n")
channel.sendall("transfer upload datatype config\n")
channel.sendall("transfer upload serverip 10.1.1.1\n")
channel.sendall("transfer upload start\n")

time.sleep(2)
channel.sendall("y\n")

time.sleep(1)
print('Name of Backup file is "{}"'.format(date))

###    End of send commands ###

time.sleep(15)

# For debug
# print(type(channel.recv(1024)))
# print('Channel buffer is :  {}'.format(channel.recv(1024)))

a = channel.recv(2048)
a = a.decode('utf-8')

# print('a is {}'.format(a))

if (len(re.findall(r'successfully', a))):
    print('*****  Success  ******')
else:
    print('*****  Something wrong!!!  *****')


channel.close()
ssh.close()
