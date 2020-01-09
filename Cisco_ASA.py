#!/usr/bin/env python3.6

import paramiko
import time
import re


print('#########  Script started at: {}  #########'.format(time.strftime("%d-%m-%Y %H:%M:%S")))
date = time.strftime("%m-%d-%Y")


host = '10.1.2.1'
user = 'username'
port = 22
key_path = '/home/username/.ssh/id_rsa'
passphrase_ssh = 'xx'
ssh = paramiko.SSHClient()
# add server key to known
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(hostname=host, username=user, key_filename=key_path, port=port, passphrase=passphrase_ssh) # , passphrase=passphrase_ssh)
    time.sleep(1)
except paramiko.ssh_exception.NoValidConnectionsError:
    logger.debug("Could not connect to host {}".format(host))
    print("Could not connect to host {}".format(host))
except Exception as e:
    print("Some error: %s" % e)
    raise SystemExit(2)

# print("channel.sendall('backup /noconfirm interface Servers passphrase yyy location tftp://10.1.1.1/ASA/{}\n'.format(date))")

ssh.connect(hostname=host, username=user, port=port, key_filename=key_path, passphrase=passphrase_ssh)

print(' ssh connected')

channel = ssh.get_transport().open_session()
# channel.get_pty()
channel.settimeout(50)
channel.invoke_shell()

while channel.recv_ready():
    channel.recv(1024)

###    Start to sends commands ###


channel.sendall("en 3\n")
time.sleep(1)

channel.sendall("xxx\n")
time.sleep(1)

channel.sendall('backup /noconfirm interface Servers passphrase yyy location tftp://10.1.1.1/ASA/\n')
time.sleep(100)

###    End of send commands ###

# For debug
#print('*******************************************')
#print('Channel buffer is :  {}'.format(channel.recv(2048)))

a = channel.recv(2048)
a = a.decode('utf-8')

#print('a is {}'.format(a))

if (len(re.findall(r'ished!', a))):
    print('*****  Success  ******')
else:
    print('*****  Something wrong!!!  *****')

channel.close()
ssh.close()