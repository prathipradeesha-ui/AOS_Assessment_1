# Advanced Operating Systems - Assessment 1

## Project Overview

This repository contains three scripting-based tasks developed for Advanced Operating Systems Assessment 1.

The project demonstrates operating system concepts including process management, scheduling algorithms, file system operations, automation, authentication, and logging using Bash and Python in a Linux environment.

---

# Task 1 - Smart Campus IoT Device Management System

## Description

A Bash-based system administration tool that simulates managing Linux-based IoT gateway devices.

The system provides automated monitoring and management features for campus IoT sensor environments.

## Features

- CPU and memory usage monitoring
- Display top ten memory-consuming processes
- Process termination with user confirmation
- Protection of critical system processes
- Sensor log file management
- Detection of large log files
- Log compression and archival
- Timestamped archive creation
- Administrative activity logging

## Execution

```bash
cd Task1_IoT
chmod +x smart_campus.sh
./smart_campus.sh
```

---

# Task 2 - University Research Cluster Job Scheduler

## Description

A Bash/Python-based job scheduling system that manages computational job requests using operating system scheduling concepts.

The system demonstrates queue management, scheduling algorithms, and job execution tracking.

## Features

- Submit job requests
- View pending jobs
- Process job queue
- View completed jobs
- Queue management
- Scheduling event logging
- Job execution tracking

## Scheduling Algorithms

The system implements:

- Round Robin Scheduling
- Priority Scheduling

## Data Storage

The system maintains:

- `job_queue.txt` - Stores pending job requests
- `completed_jobs.txt` - Stores completed jobs
- `scheduler_log.txt` - Stores scheduling activities

## Execution

```bash
cd Task2_JobScheduler
python3 scheduler.py
```

---

# Task 3 - Secure Student Project Submission and Authentication System

## Description

A secure project submission management system that validates student files and monitors authentication activities.

The system provides security controls to prevent invalid submissions and detect suspicious access attempts.

## Features

- Assignment submission
- PDF and DOCX file validation
- File size checking
- Duplicate submission detection
- Login attempt simulation
- Failed login monitoring
- Account locking after repeated failures
- Suspicious activity detection
- Audit logging

## Data Storage

The system maintains:

- `submission_log.txt` - Records submission and login activities

## Execution

```bash
cd Task3_Submission
python3 submission_system.py
```

---

# Technologies Used

- Ubuntu Linux / WSL2
- Bash Shell Scripting
- Python Programming
- POSIX Command Line Tools
- Linux File System Management
- Git Version Control
- GitHub Repository Management

---

# Version Control

Git was used throughout the development process to maintain source code history and track project progress.

The repository contains commits showing the development stages of:

- Task 1 Smart Campus IoT Device Management System
- Task 2 Research Cluster Job Scheduler
- Task 3 Secure Student Project Submission System
- README documentation updates

---

# Learning Outcomes Covered

## LO2

Applied operating system management techniques including process monitoring, automation, file management, and system control.

## LO4

Applied UNIX command line tools and advanced shell scripting techniques within a POSIX compliant environment.
