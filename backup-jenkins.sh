#!/bin/bash

BACKUP_DIR="$HOME/jenkins-backups"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/jenkins-backup-$DATE.tar.gz"

mkdir -p "$BACKUP_DIR"

tar -czf "$BACKUP_FILE" -C "$HOME/jenkins-data" .

if [ $? -eq 0 ]; then
    echo "Backup created successfully: $BACKUP_FILE"
else
    echo "Backup failed!"
    exit 1
fi

find "$BACKUP_DIR" -type f -name "jenkins-backup-*.tar.gz" -mtime +7 -delete
