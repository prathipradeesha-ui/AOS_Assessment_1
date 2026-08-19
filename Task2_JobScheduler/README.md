# University Research Cluster Job Scheduler

## Advanced Operating Systems – Assessment 1

### Overview

This project implements a menu-driven University Research Cluster Job Scheduler using Python. The system manages computational job requests submitted by students and processes them using different operating system scheduling algorithms.

The scheduler demonstrates job queue management, Round Robin scheduling, Priority Scheduling, execution tracking, input validation, and event logging.

## Requirements

* Linux / Ubuntu / WSL
* Python 3
* Python standard libraries

## How to Run

Navigate to the Task 2 directory:

```bash
cd ~/AOS_Assessment_1/Task2_JobScheduler
```

Run the scheduler:

```bash
python3 job_scheduler.py
```

## Main Features

### 1. View Pending Jobs

Displays all jobs currently waiting in the job queue, including:

* Student ID
* Job name
* Estimated execution time
* Priority

### 2. Submit Job Request

Allows a student to submit a computational job by entering:

* Student ID
* Job name
* Estimated execution time
* Priority from 1 to 10

Priority 1 represents the highest priority.

### 3. Process Job Queue

The system provides two scheduling algorithms:

#### Round Robin Scheduling

Round Robin uses a fixed time quantum of 5 seconds. Jobs are processed fairly by giving each job a limited execution time before moving to the next job.

#### Priority Scheduling

Priority Scheduling processes jobs according to their priority. A lower priority number represents a higher priority.

### 4. View Completed Jobs

Displays jobs that have been successfully processed and completed.

### 5. Exit

Safely exits the scheduler application.

## Files

| File                 | Description                          |
| -------------------- | ------------------------------------ |
| `job_scheduler.py`   | Main Python scheduler program        |
| `job_queue.txt`      | Stores pending job requests          |
| `completed_jobs.txt` | Stores completed jobs                |
| `scheduler_log.txt`  | Stores scheduler activity and events |
| `README.md`          | Project documentation                |

## Logging

The scheduler records important events in `scheduler_log.txt`, including job submissions, scheduling activity, job execution, and completion.

## Scheduling Demonstration

The system can be demonstrated by:

1. Submitting multiple jobs with different priorities.
2. Viewing the pending job queue.
3. Selecting Priority Scheduling.
4. Observing jobs processed according to priority.
5. Submitting additional jobs.
6. Selecting Round Robin Scheduling.
7. Viewing the completed jobs.
8. Checking the scheduler log.

## Operating System Concepts

This task demonstrates important operating system concepts including:

* Process and job scheduling
* CPU scheduling algorithms
* Round Robin scheduling
* Priority Scheduling
* Queue management
* Execution tracking
* Logging
* Input validation

