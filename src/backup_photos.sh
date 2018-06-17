#!/bin/bash 

# This script needs custom modification for each user.

################################################################################
# MOUNT FOLDERS AS NECESSARY 

echo "Mounting NAS"
mount /media/diskstation/photo
sleep 10


################################################################################
# SET FOLDERS (IMPORTANT: INCLUDE TRAILING SLASH)

# Source and destination folders
SRC=/media/sigma/PhotoDisk/
DEST=/media/diskstation/photo/PhotoDisk/

# Log folder
LOG=/media/diskstation/photo/log/

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
# CHECK IF FOLDERS EXISTS

if [ ! -d "$SRC" ]; then
	echo "Source not found: $SRC"
	exit 1
fi

if [ ! -d "$DEST" ]; then
	echo "Destination not found: $DEST"
	exit 1
fi

if [ ! -d "$LOG" ]; then
	echo "Log folder not found: $LOG"
	exit 1
fi

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
