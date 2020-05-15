# Network backup sceipts

This is just a one way to make backup configs from Cisco with python

## Getting Started

This project consist of several scripts witch allows you do the next things:
* backup config from cisco devices ( and extreme 210 )
* compare backups of configs and remove the identical files
* send result in slack

Each part has own scripts:

1. Scripts to backup:
star:
  - Cisco_SW.py
  - Cisco_ASA.py 
  - Extreme_210.py 	
  - ME_Controller.py
2. Scripts to compare backups:
star:
  - backpy_diff.py
3. Script to analyze logs from previos stages and send notification to Slack:
star:
  - slack.py

### Prerequisites

All this scripts was developed to use at any unix-like system. 

To make it work you need a 
`python v3.6 ` [How install python 3](https://realpython.com/installing-python/)
`crontab` The software utility cron is a time-based job scheduler in Unix-like computer operating systems. Ususally installed default

```
python3.6 --version
crontab ?
```

### Installing

Create folder 
```
~/scripts && cd ~/scripts
```
Clone project  
```
git clone git@github.com:Andrey-cisco/network_backup_scripts.git && cd network_backup_scripts
```
make this scripts executable
```
chmod +x * && chmox +x result/*
```

### Configuration crontab

To make this scripts executable onece a day type from user whitch will be start this scripts: 

```
crontal -e 
```
Backup configs
```
0 9 * * * /usr/bin/python3.6 -q ~/scripts/Cisco_ASA.py >>  /home/user/mount/tftp/logs/asa.log 
0 9 * * * /usr/bin/python3.6 -q ~/scripts/Cisco_SW.py >>   /home/user/mount/tftp/logs/sw.log 
1 9 * * * /usr/bin/python3.6 -q ~/scripts/ME_Controller.py >>  /home/user/mount/tftp/logs/ME.log 
```
Then start backpy_diff.py to delete equal files
```
10 9 * * * /usr/bin/python3.6 -q ~/scripts/result/diff.py >>  /home/user/mount/tftp/logs/diff.log
```
Then result.py analyze logs from and create "brief" file which contain result of scripts work
```
15 9 * * * /usr/bin/python3.6 -q ~/scripts/result/result.py >>  /home/user/mount/tftp/logs/result.log
```
And send result to Slack
59 9 * * * /usr/bin/python3.6 -q /home/backup/scripts/result/slack.py >>  /home/backup/mount/tftp/logs/slack.log


### Tests 

First of all you have an opportunity to connent with ssh from user witch will make scripts and have an access to ssh key

Then you can try start all scripts for backup malualy:
```
/usr/bin/python3.6 -q ~/scripts/Cisco_ASA.py
```
If all if fine you see the next:
```
#########  Script started at: 15-05-2020 10:34:16  #########
 ssh connected
*****  Success  ******
```

Then you can start diff 
```
/usr/bin/python3.6 -q ~/scripts/result/diff.py
```

If there is no files to compare you'll see en error:
```
####  File in ASA/* not found  #####
ASA diff crashed
*** diff in ASA is ended ***
```

If filres the same : 
```
Files of Extreme backup the same
home/user/05-13-2020 removed
*** diff in Extreme is ended ***
```

If files has differents: 
```
ME_MO backup has Different files
*** diff in ME_MO is ended ***
```

### Troubleshooting

If you need to understand what's going on at cisco you can uncomment line
```
#print('Channel buffer is :  {}'.format(channel.recv(2048)))
```
or 
```
#print('a is {}'.format(a))
```

And you'll see output from cisco side.


Also you can show result of "result.py" script whitch at the end will send to slack
```
cat /home/user/scripts/result/brief

#  Script start at 09:15:01 01-01-2020 
# 
# Result for backup of ASA is *****  Success  ******
# 
# Result for backup of ME is *****  Success  ******
# 
# Result for backup of SW1 is *****  Success  ******
```


## Deployment

You need generate [ssh keys](https://www.ssh.com/ssh/keygen/) and move public key to cisco devices to have an option to connect to devices with ssh keys. Otherwise you can use username\password and make changes in scripts into module **ssh.connect**

Also Yoy need generate tocken for web hook to send something into slack [Webhooks](https://api.slack.com/messaging/webhooks) 

And of course you need create **acl** to have an access devices with ssh

**Before start diff.py you have to start scripts to backup ( files witch will be compared should exist )**


## Versioning

You can make forks and you [SemVer](http://semver.org/) for versioning. 

## Authors

* **Andrey Trushchelev** - *Initial work* - [Linkedin](https://www.linkedin.com/in/andrey-trushchelev/)

See also my public projects at [GitLab](https://gitlab.com/TrueAndrD)

## License

This project has free licence.

![Free](https://www.sialicencehub.co.uk/wp-content/uploads/2013/06/Free-sia-licence-training-300x142.jpg)

## Acknowledgments

You can add similar script to this repo to make backup from another devices and share it with a world! 
With a luck!

