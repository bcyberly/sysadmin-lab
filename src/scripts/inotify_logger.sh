#!/bin/bash
# Purpose: Monitor a directory for file events and log them with timestamps.
# Usage: ./inotify_logger.sh [directory] [logfile]

WATCH_DIR="${1:-/tmp/test_monitor}"
LOG_FILE="${2:-inotify_events.log}"

# Create watch direcotry if it doesnt exist
mkdir -p "$WATCH_DIR"

echo "Monitoring $WATCH_DIR. Events will be logged to $LOG_FILE"
echo "Started at $(date)" >> "$LOG_FILE"

# Monitor and log

inotifywait -m "$WATCH_DIR" -e create -e modify -e delete -e move \
    --format '%T %w%f %e' --timefmt '%Y-%m-%d %H:%M:%S' | while read event
    do
        echo "$event" >> "LOG_FILE"
        echo "$event" # also show on console
    done