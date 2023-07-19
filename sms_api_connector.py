import requests, variables

def sendSMS():
    print("called sendSMS")
    url = "https://sms.8x8.com/api/v1/subaccounts/RSCompany_6lLA8_hq/messages"

    payload = {
        "source": "8x8",
        "destination": "6597209504",
        "text": "From Python Function",
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer " + variables.BearerToken
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)



def sendOTP():
    print("called sendSMS")
    url = "https://sms.8x8.com/api/v1/subaccounts/RSCompany_6lLA8_hq/messages"

    payload = {
        "source": "8x8",
        "destination": "6597209504",
        "text": "abc123",
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer " + variables.BearerToken
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)