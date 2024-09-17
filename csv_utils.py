import csv
from typing import Dict

def read_from_csv(file_path: str, csv_location="emails.csv") -> Dict:
    with open(csv_location, "r") as csv_file:
        reader = csv.reader(csv_file)
        emails_dict = {rows[0]: rows[1] for rows in reader}

    return emails_dict
