import pandas as pd
import time
from llm import generate_email
from email_sender import send_email
from logger import log_result

def run():
    df = pd.read_csv("leads.csv")

    for _, row in df.iterrows():
        name = row["name"]
        email = row["email"]
        company = row["company"]
        role = row["role"]

        print(f"Processing {name}...")

        try:
            message = generate_email(name, company, role)

            success = send_email(
                email,
                subject="Quick idea for your team",
                body=message
            )

            status = "SENT" if success else "FAILED"
            log_result(name, email, status)

            print(f"{status} → {email}")

            time.sleep(2)  # avoid spam limits

        except Exception as e:
            print(f"Error: {e}")
            log_result(name, email, "ERROR")

if __name__ == "__main__":
    run()
