Scrypts to backup config from cisco devices ( and extreme 210 )
  Cisco_SW.py
  Cisco_ASA.py 
	Extreme_210.py 	
	ME_Controller.py

In result folder
  backpy_diff.py - compare backups and remove the identical files
  result.py - create file "brief" which contain result of backup scripts
  slack.py - send file "brief" to slack


***

Scripts analyze logs from backup scripts which make backup from network devices and send result in slack

We have crontab on server which run backup_srcipts
And we have logs as result of this scripts:

crontab -l
0 5 * * * /usr/bin/python3.6 -q /home/user/scripts/backpy_asa >>  /home/user/mount/tftp/logs/asa.log 
0 5 * * * /usr/bin/python3.6 -q /home/user/scripts/backpy_sw >>   /home/user/mount/tftp/logs/sw.log 
1 5 * * * /usr/bin/python3.6 -q /home/user/scripts/backpy_ME >>  /home/user/mount/tftp/logs/ME.log 

Then backpy_diff.py delete equal files
10 5 * * * /usr/bin/python3.6 -q /home/user/scripts/backpy_diff >>  /home/user/mount/tftp/logs/diff.log

Then result.py analyze logs from logs and create brief file which contain result of scripts work
15 5 * * * /usr/bin/python3.6 -q /home/user/scripts/result/result.py >>  /home/user/mount/tftp/logs/result.log

cat /home/user/scripts/result/brief

#  Script start at 05:15:01 09-01-2020 
# 
# Result for backup of ASA is *****  Success  ******
# 
# Result for backup of ME is *****  Success  ******
# 
# Result for backup of SW1 is *****  Success  ******

Finaly slack.py send message of result to slack
59 8 * * * /usr/bin/python3.6 -q /home/user/scripts/result/slack.py >>  /home/user/mount/tftp/logs/slack.log 

