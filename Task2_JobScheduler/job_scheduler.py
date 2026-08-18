
import os
import time
from datetime import datetime


QUEUE_FILE = "job_queue.txt"
COMPLETED_FILE = "completed_jobs.txt"
LOG_FILE = "scheduler_log.txt"


def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} | {message}\n")


def display_title():
    print("\n====================================")
    print(" UNIVERSITY RESEARCH CLUSTER SCHEDULER")
    print("======================================")

def submit_job():
    print("\n--- Submit New Job ---")

    student_id = input("Enter Student ID: ")
    job_name = input("Enter Job Name: ")
    
    while True:
        try:
            execution_time = int(input("Enter Estimated Execution Time (seconds): "))
            if execution_time > 0:
                break
            else:
                print("Execution time must be positive.")
        except ValueError:
            print("Enter a valid number.")

    while True:
        try:
            priority = int(input("Enter Priority (1-10, 1 highest): "))
            if 1 <= priority <= 10:
                break
            else:
                print("Priority must be between 1 and 10.")
        except ValueError:
            print("Enter a valid number.")

    job = f"{student_id},{job_name},{execution_time},{priority}"

    with open(QUEUE_FILE, "a") as file:
        file.write(job + "\n")

    log_event(
        f"Job Submitted | Student ID: {student_id} | "
        f"Job: {job_name} | Priority: {priority}"
    )

    print("Job submitted successfully.")



def view_pending_jobs():
    print("\n--- Pending Jobs ---")

    if not os.path.exists(QUEUE_FILE):
        print("No pending jobs.")
        return

    with open(QUEUE_FILE, "r") as file:
        jobs = file.readlines()

    if len(jobs) == 0:
        print("No pending jobs.")
        return

    print("\nStudent ID | Job Name | Execution Time | Priority")
    print("-" * 55)

    for job in jobs:
        if not job.strip():
            continue

        student_id, job_name, execution_time, priority = job.strip().split(",")

        print(
            f"{student_id} | {job_name} | "
            f"{execution_time}s | Priority {priority}"
        )






def load_jobs():
    jobs = []

    if os.path.exists(QUEUE_FILE):
        with open(QUEUE_FILE, "r") as file:
            for line in file:
                if line.strip():
                    student_id, job_name, execution_time, priority = line.strip().split(",")

                    jobs.append({
                        "student_id": student_id,
                        "job_name": job_name,
                        "execution_time": int(execution_time),
                        "priority": int(priority)
                    })

    return jobs


def save_completed(job, scheduling_type):
    with open(COMPLETED_FILE, "a") as file:
        file.write(
            f"{job['student_id']},{job['job_name']},"
            f"{job['execution_time']}s,"
            f"Priority {job['priority']},"
            f"{scheduling_type}\n"
        )

    log_event(
        f"Job Executed | Student ID: {job['student_id']} | "
        f"Job: {job['job_name']} | "
        f"Scheduling: {scheduling_type} | Completed"
    )



def priority_scheduling():

    jobs = load_jobs()

    if not jobs:
        print("No jobs available.")
        return

    print("\n--- Priority Scheduling ---")

    jobs.sort(key=lambda x: x["priority"])

    for job in jobs:
        print(
            f"Executing {job['job_name']} "
            f"(Priority {job['priority']})"
        )

        time.sleep(job['execution_time'])

        save_completed(job, "Priority")

    open(QUEUE_FILE, "w").close()

    print("Priority scheduling completed.")




def round_robin():

    jobs = load_jobs()

    if not jobs:
        print("No jobs available.")
        return

    print("\n--- Round Robin Scheduling ---")

    quantum = 5

    while jobs:

        for job in jobs[:]:

            if job["execution_time"] > 0:

                run_time = min(
                    quantum,
                    job["execution_time"]
                )

                print(
                    f"Running {job['job_name']} "
                    f"for {run_time} seconds"
                )

                time.sleep(run_time)

                job["execution_time"] -= run_time


            if job["execution_time"] <= 0:

                print(
                    f"{job['job_name']} completed"
                )

                save_completed(job, "Round Robin")

                jobs.remove(job)


    open(QUEUE_FILE, "w").close()

    print("Round Robin scheduling completed.")





def view_completed_jobs():
    print("\n--- Completed Jobs ---")

    if not os.path.exists(COMPLETED_FILE):
        print("No completed jobs.")
        return

    with open(COMPLETED_FILE, "r") as file:
        jobs = file.readlines()

    if len(jobs) == 0:
        print("No completed jobs.")
        return

    for job in jobs:
        print(job.strip())





def main():

    while True:

        display_title()

        print("1. View Pending Jobs")
        print("2. Submit Job Request")
        print("3. Process Job Queue")
        print("4. View Completed Jobs")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_pending_jobs()

        elif choice == "2":
            submit_job()

        elif choice == "3":

            print("\nSelect Scheduling Method")
            print("1. Round Robin")
            print("2. Priority Scheduling")

            method = input("Enter option: ")

            if method == "1":
                round_robin()

            elif method == "2":
                priority_scheduling()

            else:
                print("Invalid scheduling option.")

        elif choice == "4":
            view_completed_jobs()

        elif choice == "5":

            confirm = input(
                "Are you sure you want to exit? (Y/N): "
            )

            if confirm.lower() == "y":
                print("Bye!")
                break

        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main()
