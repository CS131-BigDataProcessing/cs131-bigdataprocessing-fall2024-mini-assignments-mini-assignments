
This assignment involves creating and managing automated tasks using cron. The tasks include daily file cleanup, weekly system backups, and automated disk usage reports sent via email. 
Below are the details of each cron job and how to set them up.


This cron job deletes all files from the specified temporary directory every day at 2:00 AM.
0 2 * * * /bin/rm -rf /path/to/home/temp/*


This cron job automates the backup of the home directory every Sunday at 3:00 AM. It uses the tar command to compress the contents of the home directory and stores the backup in a designated folder.
0 3 * * 0 /bin/tar -czf /path/to/home/user/backups/home_backup_$(date +\%F).tar.gz /path/to/home/user/

This cron job sends a daily disk usage report at 8:30 AM. The report includes the output of the df -h command and is sent to a specified email address.

30 8 * * * /bin/df -h | mail -s "Daily Disk Usage Report" youremail@email.com. 


To edit your cron jobs, open the crontab editor by running this command
crontab -e

Add cronjobs by using 
crontab -l

File contains: 
crontab: A copy of the cron jobs scheduled for this assignment.
about_crontask.txt: A text file that answers questions related to cron tasks and their benefits/risks.
