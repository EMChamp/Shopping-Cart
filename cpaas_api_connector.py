import requests, variables
smsSubaccount = variables.sms_subaccount
smsSenderId = variables.sms_sender_id
voiceCaller = variables.voice_caller_number
voiceSubaccount = variables.voice_subaccount

headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer " + variables.BearerToken
}

def sendSMS(phone_number):
    url = f"https://sms.8x8.com/api/v1/subaccounts/{smsSubaccount}/messages"

    payload = {
        "source": smsSenderId,
        "destination": phone_number,
        "text": "Your order is on its way!",
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)



def sendOTP(phone_number):
    url = f"https://sms.8x8.com/api/v2/subaccounts/{smsSubaccount}/sessions"

    payload = {
        "destination": phone_number,
        "sms": {
            "source": smsSenderId,
            "encoding": "AUTO"
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()
    return response_data["sessionId"]


def verifyOTP(sessionID, otpCode):
    url = f"https://verify.8x8.com/api/v2/subaccounts/{smsSubaccount}/sessions/" + sessionID + "?code=" + otpCode

    response = requests.get(url, headers=headers)
    response_data = response.json()
    print(response_data)
    return response_data["status"] == "VERIFIED"

def makeCall(phone_number):
    url = f"https://voice.wavecell.com/api/v1/subaccounts/{voiceSubaccount}/callflows"

    payload = {
        "callflow": [
            {
            "action": "makeCall",
            "params": {
                "source": voiceCaller,
                "destination": phone_number
                }
            },
            {
            "action": "say",
            "params": {
                "text": "Hello, please confirm your availability for a delivery today at 5PM.",
                "voiceProfile": "en-IE-EmilyNeural",
                "repetition": 1,
                "speed": 1
                }
            },
            {
            "action": "hangup"
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()
    return response_data