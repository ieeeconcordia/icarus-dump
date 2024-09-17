import os
from typing import List
import requests
from dotenv import load_dotenv

import csv_utils

def send_templated_message(api_key: str, template_name: str, to_contact: List[str], from_contact: str, subject: str):
	try:
		requests.post(
		"https://api.mailgun.net/v3/mv.ieeeconcordia.ca/messages",
		auth=("api", api_key),
		data={"from": from_contact,
			"to": to_contact,
			"subject": subject,
			"template": template_name,
			})
	except Exception as e:
		print(f"Error sending email: {e}")

def transform_email_dict_to_contact_list(email_dict: dict):
	contact_list = []
	
	for key, value in email_dict.items(): # key is the email, value is the timestamp
		contact_list.append(f"<{key}>")
	
	return contact_list


if __name__ == "__main__":
	load_dotenv()
	
	api_key = os.getenv("SINCH_MAILGUN_API_KEY")
	template_name = "mission brief: green thumb"
	to_contacts = transform_email_dict_to_contact_list(csv_utils.read_from_csv("emails.csv"))
	from_contact = "Icarus <icarus@mv.ieeeconcordia.ca>"
	subject = "Mission Brief: Green Thumb"

	send_templated_message(api_key, template_name, to_contacts, from_contact, subject)
	
