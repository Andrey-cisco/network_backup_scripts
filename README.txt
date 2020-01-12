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
0 9 * * * /usr/bin/python3.6 -q /home/user/scripts/Cisco_ASA.py >>  /home/user/mount/tftp/logs/asa.log 
0 9 * * * /usr/bin/python3.6 -q /home/user/scripts/Cisco_SW.py >>   /home/user/mount/tftp/logs/sw.log 
1 9 * * * /usr/bin/python3.6 -q /home/user/scripts/ME_Controller.py >>  /home/user/mount/tftp/logs/ME.log 

Then backpy_diff.py delete equal files
10 9 * * * /usr/bin/python3.6 -q /home/user/scripts/diff.py >>  /home/user/mount/tftp/logs/diff.log

Then result.py analyze logs and create "brief" file which contain result of scripts work
15 9 * * * /usr/bin/python3.6 -q /home/user/scripts/result/result.py >>  /home/user/mount/tftp/logs/result.log

Example of result "result.py" script:

cat /home/user/scripts/result/brief

#  Script start at 09:15:01 01-01-2020 
# 
# Result for backup of ASA is *****  Success  ******
# 
# Result for backup of ME is *****  Success  ******
# 
# Result for backup of SW1 is *****  Success  ******

Finaly slack.py send message which contain "brief" file to slack
59 9 * * * /usr/bin/python3.6 -q /home/user/scripts/result/slack.py >>  /home/user/mount/tftp/logs/slack.log 

