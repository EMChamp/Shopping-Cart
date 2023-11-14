# Shopping Cart  
This ecommerce example is modified to show how to use 8x8's SMS and Video APIs.
  
## Dependencies ##
1. Python3
2. Several packages in requirements.txt (taken care of as part of "How to Run")
3. An 8x8 Subaccount/API Key

## How to run ##
0. Modify Variables.py with your 8x8 credentials such as: voice/sms subaccounts, api keys, sms sender id and voice phone number.
1. Create Virtual Environment - python3 -m venv myenv
2. Use Virtual Environment - source myenv/bin/activate
3. Install Requirements - pip install -r requirements.txt
4. Run the server - pipenv run python main.py
5. Enter localhost:80 in the browser (Note: Edit app.py to use a different port if it is already taken)

## How to run as a Docker Container ##
You can also opt to build the provided dockerfile, note that it uses the files in the directory so any changes you make to the application should be used in the docker container.