# Secure Student Project Submission and Authentication System

## Advanced Operating Systems – Assessment 1

### Overview

This project implements a menu-driven Secure Student Project Submission and Authentication System using Python. The system validates student assignment submissions and records submission and authentication activities through an audit log.

The system demonstrates file validation, file size checking, duplicate submission detection, authentication monitoring, failed login detection, account locking, suspicious activity detection, and event logging.

## Requirements

* Linux / Ubuntu / WSL
* Python 3
* Python standard libraries

## How to Run

Navigate to the Task 3 directory:

```bash
cd ~/AOS_Assessment_1/Task3_Submission
```

Run the submission system:

```bash
python3 submission_system.py
```

## Main Features

### 1. Assignment Submission

Allows students to submit project files by providing their Student ID and filename.

The system validates the submission before accepting it.

### 2. File Type Validation

The system accepts the following file types:

* PDF (`.pdf`)
* Microsoft Word document (`.docx`)

Other file types are rejected.

### 3. File Size Validation

The system checks the size of the submitted file and rejects files larger than the permitted 5 MB limit.

### 4. Duplicate Submission Detection

The system checks whether a student has already submitted a file with the same filename and prevents duplicate submissions.

### 5. Authentication Monitoring

The system simulates student authentication and records login activities.

### 6. Failed Login Monitoring

Failed authentication attempts are recorded in the system log.

### 7. Account Locking

The system locks an account after three failed login attempts to help prevent repeated unauthorized access.

### 8. Suspicious Activity Detection

Repeated failed authentication attempts are monitored and recorded as suspicious activity.

### 9. Audit Logging

Submission and authentication events are recorded in:

```text
submission_log.txt
```

The log provides a record of successful submissions, rejected submissions, login attempts, and security-related events.

## Files

| File                   | Description                                       |
| ---------------------- | ------------------------------------------------- |
| `submission_system.py` | Main Python submission and authentication program |
| `submission_log.txt`   | Records submission and authentication activities  |
| `submissions/`         | Stores accepted student submission files          |
| `upload_files/`        | Stores test files used during submission testing  |
| `README.md`            | Project documentation                             |

## Submission Validation

Before accepting a file, the system checks:

1. Student ID
2. Filename
3. File extension
4. File existence
5. File size
6. Duplicate submissions

Only valid submissions are accepted.

## Security Features

The system demonstrates basic security controls including:

* File type validation
* File size restrictions
* Duplicate submission prevention
* Login attempt monitoring
* Account locking after three failed attempts
* Suspicious activity logging
* Audit trail maintenance

## Example Execution

Start the program:

```bash
python3 submission_system.py
```

The user can select the available menu options to submit an assignment, test authentication, view logs, and exit the system.

## Operating System Concepts

This task demonstrates operating system and security-related concepts including:

* File system management
* File validation
* Access control
* Authentication
* Process and event logging
* Security monitoring
* Automation
* Input validation

## Technologies Used

* Python 3
* Linux / Ubuntu / WSL
* POSIX file system
* Git and GitHub


