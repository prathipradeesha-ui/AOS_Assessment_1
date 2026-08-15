#!/bin/bash

# Smart Campus IoT Device Management System
# Advanced Operating Systems - Assessment 1

LOG_FILE="system_monitor_log.txt"

# Save an action to the log file with timestamp
log_action() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Display CPU and memory information
show_system_usage() {
    clear
    echo "========== SYSTEM USAGE =========="
    echo
    echo "--- Memory Usage ---"
    free -h
    echo
    echo "--- CPU Load ---"
    uptime

    log_action "Checked CPU and memory usage"

    echo
    read -p "Press Enter to go back..."
}

# Display top 10 processes using memory
show_top_memory() {
    clear
    echo "========== TOP 10 MEMORY PROCESSES =========="
    echo
    printf "%-8s %-12s %-8s %-8s %s\n" "PID" "USER" "%CPU" "%MEM" "COMMAND"
    echo "--------------------------------------------------------"

    ps -eo pid,user,%cpu,%mem,comm --sort=-%mem | head -n 11 | tail -n 10

    echo
    log_action "Viewed top 10 memory consuming processes"

    read -p "Press Enter to go back..."
}

# Terminate a selected process
terminate_process() {
    clear
    echo "========== TERMINATE PROCESS =========="
    echo
    printf "%-8s %-12s %-8s %-8s %s\n" "PID" "USER" "%CPU" "%MEM" "COMMAND"
    echo "--------------------------------------------------------"

    ps -eo pid,user,%cpu,%mem,comm --sort=-%mem | head -n 11 | tail -n 10

    echo
    read -p "Enter the PID to terminate: " pid

    # Check whether PID contains only numbers
    if ! [[ "$pid" =~ ^[0-9]+$ ]]; then
        echo "Invalid PID."
        log_action "Invalid PID entered: $pid"
        read -p "Press Enter to go back..."
        return
    fi

    # Check whether the process exists
    if ! ps -p "$pid" > /dev/null 2>&1; then
        echo "Process with PID $pid was not found."
        log_action "PID $pid was not found"
        read -p "Press Enter to go back..."
        return
    fi

    # Get the process name
    process_name=$(ps -p "$pid" -o comm=)

    # Processes that should not be terminated
    protected=("systemd" "init" "sshd" "bash" "login" "kthreadd" \
               "ksoftirqd" "migration" "rcu_sched" "watchdog" "nano" "smart_campus.sh")

    for item in "${protected[@]}"; do
        if [[ "$process_name" == *"$item"* ]]; then
            echo "This is a protected process. It cannot be terminated."
            log_action "Blocked termination of $process_name PID $pid"
            read -p "Press Enter to go back..."
            return
        fi
    done

    echo
    echo "Process selected:"
    echo "PID: $pid"
    echo "Name: $process_name"

    read -p "Do you want to terminate it? (Y/N): " answer

 if [[ "$answer" == "Y" || "$answer" == "y" ]]; then
    kill "$pid" 2>/dev/null

    if [ $? -eq 0 ]; then
        sleep 1

        if ps -p "$pid" > /dev/null 2>&1; then
            echo "Termination signal sent, but process is still running."
            log_action "Process $process_name PID $pid is still running after termination attempt"
        else
            echo "Process terminated successfully."
            log_action "Terminated process $process_name PID $pid"
        fi
    else
        echo "Unable to terminate the process."
        log_action "Failed to terminate $process_name PID $pid"
    fi
else
    echo "Termination cancelled."
    log_action "Termination cancelled for PID $pid"
fi

read -p "Press Enter to go back..."

}


# Manage sensor log files
manage_logs() {
    clear
    echo "========== LOG FILE MANAGEMENT =========="
    echo

    read -p "Enter the directory containing sensor logs: " log_dir

    # Check directory
    if [ ! -d "$log_dir" ]; then
        echo "Directory does not exist."
        log_action "Log directory not found: $log_dir"
        read -p "Press Enter to go back..."
        return
    fi

    echo
    echo "--- Directory Disk Usage ---"
    du -sh "$log_dir"

    log_action "Checked disk usage of $log_dir"

    # Create ArchiveLogs folder
    archive_dir="$log_dir/ArchiveLogs"

    if [ ! -d "$archive_dir" ]; then
        mkdir -p "$archive_dir"
        echo "ArchiveLogs folder created."
        log_action "Created ArchiveLogs folder"
    fi

    echo
    echo "Searching for .log files larger than 50MB..."

    large_files=$(find "$log_dir" -maxdepth 1 -type f -name "*.log" -size +50M 2>/dev/null)

    if [ -z "$large_files" ]; then
        echo "No large log files found."
        log_action "No log files larger than 50MB found"
    else
        echo "Large log files:"
        echo "$large_files"
        echo

        current_time=$(date '+%Y%m%d_%H%M%S')

        for file in $large_files; do
            filename=$(basename "$file")
            archive_file="${filename%.*}_${current_time}.tar.gz"

            tar -czf "$archive_dir/$archive_file" -C "$log_dir" "$filename"

            echo "Archived: $filename"
            log_action "Archived $filename as $archive_file"
        done
    fi

    # Check ArchiveLogs size
    archive_size=$(du -sb "$archive_dir" 2>/dev/null | cut -f1)
    one_gb=$((1024 * 1024 * 1024))

    echo

    if [ "$archive_size" -gt "$one_gb" ]; then
        echo "WARNING: ArchiveLogs is larger than 1GB."
        log_action "ArchiveLogs exceeded 1GB"
    else
        echo "ArchiveLogs is within the 1GB limit."
    fi

    read -p "Press Enter to go back..."
}

# Main menu
while true
do
    clear

    echo "=============================================="
    echo " SMART CAMPUS IoT DEVICE MANAGEMENT"
    echo "=============================================="
    echo "1. Display CPU and Memory usage"
    echo "2. List top 10 memory consuming processes"
    echo "3. Terminate a process"
    echo "4. Log File Management and Archival"
    echo "5. View system monitor log"
    echo "6. Bye (Exit)"
    echo "=============================================="

    read -p "Enter your choice [1-6]: " choice

    case $choice in

        1)
            show_system_usage
            ;;

        2)
            show_top_memory
            ;;

        3)
            terminate_process
            ;;

        4)
            manage_logs
            ;;

        5)
            clear

            echo "========== SYSTEM MONITOR LOG =========="
            echo

            if [ -f "$LOG_FILE" ]; then
                cat "$LOG_FILE"
            else
                echo "No log entries yet."
            fi

            echo
            read -p "Press Enter to go back..."
            ;;

        6)
            echo
            read -p "Are you sure you want to exit? (Y/N): " confirm

            if [[ "$confirm" == "Y" || "$confirm" == "y" ]]; then
                log_action "User exited the system (Bye)"
                echo "Bye! System administration session ended."
                exit 0
            else
                echo "Exit cancelled."
                sleep 1
            fi
            ;;

        *)
            echo "Invalid choice. Please select 1-6."
            sleep 2
            ;;

    esac
done
