import libsql_experimental as libsql
import os
import csv
from dotenv import load_dotenv


def main(url, auth_token, csv_location="emails.csv"):
    conn = libsql.connect("registration.db", sync_url=url, auth_token=auth_token)
    conn.sync()

    emails_dict = conn.execute("select * from emails;").fetchall()

    with open(csv_location, "w") as csv_file:
        writer = csv.writer(csv_file)

        for key, value in emails_dict:
            writer.writerow([key, value])


if __name__ == "__main__":
    load_dotenv()

    url = os.getenv("TURSO_DATABASE_URL")
    auth_token = os.getenv("TURSO_AUTH_TOKEN")

    main(url, auth_token)
