# Project: Automated Task Scheduling with Cron and At

## Overview
This project demonstrates how to automate system tasks using `cron` and `at`. The setup includes scheduling recurring tasks like file cleanup, system backups, and disk usage reports, as well as one-time notifications.

## Tasks Included:
1. **Daily File Cleanup**: Deletes all files from the `/home/dumpling/temp` directory every day at 2:00 AM.
2. **Weekly System Backup**: Backs up the home directory every Sunday at 3:00 AM and stores it in the `backups` folder.
3. **One-Time Notification**: Schedules a terminal notification to appear in 30 minutes using `at`.
4. **Disk Usage Report**: Sends a daily disk usage report via email at 8:30 AM.

## How to Use:
1. Add the cron jobs to your crontab file using `crontab -e`.
2. Ensure necessary scripts (e.g., `backup.sh`) are in place and executable.
3. Check cron job status with `crontab -l`.
