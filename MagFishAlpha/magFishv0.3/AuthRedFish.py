import getpass #used for hidden password entry
import requests #main package for making get requests
import json #used to parse the json response from redfish
import time
from Addresses import CHASSIS_PAGE #Collection of constants for redfish address templates
requests.packages.urllib3.disable_warnings()
#Due to the nature of our systems, every request will print a warning about security certificates to the terminal
#This disables the warnings from printing to cmmndline at every request

#constant for head to be sent with each request
HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

def authenticate(address):

    user = ""
    password = ""

    while user == "":
        user = input("\nPlease enter the user name for the server: ")
    while password == "":
        #takes input without displaying characters for more secure password entry
        password = getpass.getpass("\nPlease enter the password for the server: ")
    #construct address for chassis page based on ip address
    authAddress = CHASSIS_PAGE.replace("IP",address)
    print("\nAuthenticating...",end="")

    try:
        try:
            response = requests.get(authAddress,headers=HEADERS,verify=False,auth=(user,password))
        except Exception:
            print("\nRequest timed out. Retrying in 30 seconds...")
            time.sleep(30)
            print("Retrying...",end="")
            response = requests.get(authAddress,headers=HEADERS,verify=False,auth=(user,password))

        try:
            json_response = json.loads(response.text)
            print("Successful")
            credentials = [user,password]
            return credentials
        except Exception:
            failed = True
            print("Failed")
            print("\nAre you sure you entered the correct user and password?")
    except Exception as error:
        print(error)
