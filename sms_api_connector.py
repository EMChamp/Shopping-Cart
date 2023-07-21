import requests, variables
destination = "6597209504"

headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer " + variables.BearerToken
}

def sendSMS():
    url = "https://sms.8x8.com/api/v1/subaccounts/RSCompany_6lLA8_hq/messages"

    payload = {
        "source": "8x8",
        "destination": destination,
        "text": "Your order is on its way!",
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)



def sendOTP():
    print("send OTP")
    url = "https://sms.8x8.com/api/v2/subaccounts/RSCompany_6lLA8_hq/sessions"

    payload = {
        "destination": destination,
        "sms": {
            "source": "8x8",
            "encoding": "AUTO"
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()
    return response_data["sessionId"]


def verifyOTP(sessionID, otpCode):
    url = "https://verify.8x8.com/api/v2/subaccounts/RSCompany_6lLA8_hq/sessions/" + sessionID + "?code=" + otpCode

    response = requests.get(url, headers=headers)
    response_data = response.json()
    print(response_data)
    return response_data["status"] == "VERIFIED"