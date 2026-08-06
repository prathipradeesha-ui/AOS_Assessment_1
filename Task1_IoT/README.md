# Smart Campus IoT Device Management System

## Advanced Operating Systems – Assessment 1

### Overview

This project implements a menu-driven Smart Campus IoT Device Management System using Bash scripting. The system provides basic operating system administration functions for monitoring processes, managing sensor log files, maintaining system logs, and safely terminating processes.

## Requirements

* Linux / Ubuntu / WSL
* Bash shell
* Standard Linux commands such as `ps`, `free`, `uptime`, `du`, `find`, `tar`, and `kill`

## How to Run

Navigate to the Task 1 directory:

```bash
cd ~/AOS_Assessment_1/Task1_IoT
```

Make sure the script is executable:

```bash
chmod +x smart_campus.sh
```

Run the application:

```bash
./smart_campus.sh
```

## Menu Options

### 1. Display CPU and Memory Usage

Displays current memory usage using `free` and CPU/load information using `uptime`.

### 2. List Top 10 Memory Consuming Processes

Displays the top ten memory-consuming processes including:

* Process ID (PID)
* User
* CPU percentage
* Memory percentage
* Command

### 3. Terminate a Process

Allows the user to select a process by PID. The system validates the PID, checks whether the process exists, protects critical processes, and requests confirmation before termination.

### 4. Log File Management and Archival

Allows the user to specify a sensor log directory. The system:

* Displays directory disk usage.
* Detects `.log` files larger than 50 MB.
* Creates an `ArchiveLogs` directory when required.
* Compresses large log files into timestamped `.tar.gz` archives.
* Displays a warning if `ArchiveLogs` exceeds 1 GB.

### 5. View System Monitor Log

Displays administrative actions recorded in `system_monitor_log.txt`. Actions are recorded with timestamps.

### 6. Bye (Exit)

The system asks for Y/N confirmation before exiting.

## Files

```text
smart_campus.sh
system_monitor_log.txt
sensor_logs/
.gitignore
README.md
```

### Main Script

`smart_campus.sh` contains the complete Bash implementation.

### System Log

`system_monitor_log.txt` records administrative actions with timestamps.

### Sensor Logs

`sensor_logs/` contains sensor log files and the `ArchiveLogs/` directory used for compressed log archives.

## Example Execution

Start the program:

```bash
./smart_campus.sh
```

The system displays a menu containing options for system monitoring, process management, log management, system logging, and exiting.

## GitHub Repository

The source code and project documentation are maintained in a private GitHub repository for the assessment.
