#!/bin/bash 

# This script needs custom modification for each user.

################################################################################
# MOUNT FOLDERS AS NECESSARY 





################################################################################
# SET FOLDERS (IMPORTANT: INCLUDE TRAILING SLASH)

# Source and destination folders
SRC=/home/sigvald/Programming/systools/src/src/
DEST=/home/sigvald/Programming/systools/src/dest/

# Log folder
LOG=/home/sigvald/Programming/systools/src/log/

################################################################################
# CHOOSE BACKUP STRATEGY

# Exact mirror on destination; delete files not existing on source.
# STRATEGY="--delete"

# Never delete files (but may overwrite updated files).
# STRATEGY=""

# Move files not on source to separate folder (preserve folder structure).
STRATEGY="--delete --backup --backup-dir=DELETED"

################################################################################
# CHOOSE DEBUG OR NOT

DEBUG="--dry-run"
# DEBUG=""

################################################################################
# EXECUTE

# Todays log file
LOG="$LOG$(date +'%Y-%m-%d').txt"

echo "Backup in progress. Do not abort. To monitor:"
echo "  tail -f $LOG"

echo "backup_photos: Backup started: $(date +'%Y-%m-%d %H:%M:%S')" &>> $LOG

rsync $DEBUG -av $STRATEGY $SRC $DEST &>> $LOG

echo "backup_photos: Backup finished: $(date +'%Y-%m-%d %H:%M:%S')" &>> $LOG

echo "Backup complete."
