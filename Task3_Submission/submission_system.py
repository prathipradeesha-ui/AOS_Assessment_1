import os
import time
import hashlib
from datetime import datetime


SUBMISSION_FOLDER = "submissions"
UPLOAD_FOLDER = "upload_files"
LOG_FILE = "submission_log.txt"


failed_attempts = {}



def log_event(message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{timestamp} | {message}\n")




def get_file_hash(path):

    hasher = hashlib.md5()

    with open(path, "rb") as file:
        hasher.update(file.read())

    return hasher.hexdigest()




def submit_assignment():

    print("\n--- Submit Assignment ---")

    student_id = input("Enter Student ID: ")
    filename = input("Enter assignment filename: ")


    file_path = os.path.join(UPLOAD_FOLDER, filename)



    # File format validation

    if not (filename.lower().endswith(".pdf") or filename.lower().endswith(".docx")):

        print("Invalid file type. Only PDF and DOCX are accepted.")

        log_event(
            f"Submission Rejected | Student ID: {student_id} | "
            f"Filename: {filename} | Invalid Format"
        )

        return




    # Check file exists

    if not os.path.exists(file_path):

        print("File not found.")

        log_event(
            f"Submission Failed | Student ID: {student_id} | "
            f"Filename: {filename} | File Not Found"
        )

        return




    # File size validation

    file_size = os.path.getsize(file_path)


    if file_size > 5 * 1024 * 1024:

        print("File too large. Maximum size is 5MB.")

        log_event(
            f"Submission Rejected | Student ID: {student_id} | "
            f"Filename: {filename} | Size Exceeded"
        )

        return




    # Duplicate detection

    destination = os.path.join(SUBMISSION_FOLDER, filename)


    if os.path.exists(destination):

        if get_file_hash(file_path) == get_file_hash(destination):

            print("Duplicate submission detected.")

            log_event(
                f"Submission Rejected | Student ID: {student_id} | "
                f"Filename: {filename} | Duplicate"
            )

            return


    import shutil

    shutil.copy2(file_path, destination)

    print("Assignment submitted successfully.")

    log_event(
        f"Submission Accepted | Student ID: {student_id} | "
        f"Filename: {filename}"
    )




def list_submissions():

    print("\n--- Submitted Assignments ---")


    files = os.listdir(SUBMISSION_FOLDER)


    if len(files) == 0:

        print("No submissions found.")

        return



    for file in files:

        print(file)





def login_attempt():

    print("\n--- Login Attempt ---")


    student_id = input("Enter Student ID: ")

    current_time = time.time()



    # Account lock checking

    if student_id in failed_attempts:

        if failed_attempts[student_id]["count"] >= 3:

            print("Account locked due to failed attempts.")

            log_event(
                f"Login Blocked | Student ID: {student_id} | Account Locked"
            )

            return




    password = input("Enter Password: ")


    correct_password = "admin123"




    if password == correct_password:


        print("Login successful.")


        failed_attempts[student_id] = {

            "count": 0,

            "last_attempt": current_time

        }


        log_event(
            f"Login Successful | Student ID: {student_id}"
        )



    else:


        print("Invalid login details.")



        if student_id not in failed_attempts:


            failed_attempts[student_id] = {

                "count": 1,

                "last_attempt": current_time

            }



        else:


            time_difference = current_time - failed_attempts[student_id]["last_attempt"]



            if time_difference < 60:


                log_event(
                    f"Suspicious Login Attempt | Student ID: {student_id}"
                )



            failed_attempts[student_id]["count"] += 1

            failed_attempts[student_id]["last_attempt"] = current_time



        log_event(
            f"Login Failed | Student ID: {student_id} | "
            f"Attempt: {failed_attempts[student_id]['count']}"
        )





def main():


    while True:


        print("\n====================================")
        print(" SECURE STUDENT PROJECT SUBMISSION SYSTEM")
        print("====================================")

        print("1. Submit Assignment")

        print("2. Check Submitted Assignment")

        print("3. List All Submissions")

        print("4. Simulate Login Attempt")

        print("5. Exit")



        choice = input("Enter your choice: ")




        if choice == "1":

            submit_assignment()



        elif choice == "2":


            filename = input("Enter filename: ")


            if os.path.exists(os.path.join(SUBMISSION_FOLDER, filename)):

                print("Assignment already submitted.")


            else:

                print("No submission found.")




        elif choice == "3":

            list_submissions()




        elif choice == "4":

            login_attempt()




        elif choice == "5":


            confirm = input("Are you sure you want to exit? (Y/N): ")


            if confirm.lower() == "y":

                print("Bye!")

                break




        else:

            print("Invalid choice.")





if __name__ == "__main__":

    main()
