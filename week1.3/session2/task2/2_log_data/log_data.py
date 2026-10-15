# Week 1.3, Session 2: Log Data Filtering

# We want to find all failed login attempts based on Request and Status code 
# (i.e., POST /login with the response 401) in a log file and print these out in a
# human-readable format.

import csv
# open and read the file
try:
    with open("week1.3/session2/task2/2_log_data/log_data.csv") as f:
        reader = csv.reader(f)
        next(reader)  # skip the header row
        
    
# find all failed login attempts (POST /login with the response 401)
        failed_logins = [row for row in reader if row[4] == "POST /login" and row[5] == "401"]
# and print these out in a human-readable format:
        for row in failed_logins:
            date, time, ip = row[0], row[1], row[2]
            print(f"IP address {ip} failed to login at {time} on {date}")
except FileNotFoundError:
            print("The log file was not found. Please check the file path.")
        
# IP address 192.168.1.17 failed to login at 10:42:12 on 2024-10-20


# Hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
# - You can use list comprehension or loops to filter the data