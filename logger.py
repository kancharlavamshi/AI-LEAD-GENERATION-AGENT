import csv
from datetime import datetime

def log_result(name, email, status):
    with open("logs.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email, status, datetime.now()])
