import csv
import requests
import time

API_KEY = "429447a6-503f-4011-a840-e5a7490b9bc4"   #write your API key
ASSISTANT_ID = "98e9e265-aa3b-455a-bf20-e037776def47"   #write your Assistant ID

def make_call(phone_number, name=None):
    url = "https://api.vapi.ai/call"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "assistantId": ASSISTANT_ID,
        "type": "outboundPhoneCall",
        "customer": {
            "number": phone_number,
            "name": name if name else "Customer"
        },
        "phoneNumberId": "9fb56d82-99c0-4560-997d-b72fbb4ed70b"     #write your Phone number ID
    }
    response = requests.post(url, json=payload, headers=headers)
    try:
        data = response.json()
    except:
        data = response.text
    print(f"📞 Calling {phone_number} -> {data}")

# CSV se numbers read karna
with open("demo.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        phone = row['Phone Number']
        name = row.get('Name', None)

        # ✅ Clean and format number
        phone = phone.strip().replace(" ", "")
        if not phone.startswith("+"):
            phone = "+91" + phone

        print(f"📞 Final dialing number: {phone}")  # Debugging

        make_call(phone, name)
        time.sleep(2)  # 2 sec gap between calls