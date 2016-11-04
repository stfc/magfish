import requests #main package for making get requests
import json #used to parse the json response from redfish

#constant for head to be sent with each request
HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
#variable for ip address of machine
address = ""
#variables for auth credentials
user = ""
password = ""

#constructs and executes a request, based on the ip provided and whether authentification is required
#returns the response
def get(baseAddress,authRequired):
    if address == "":
        print("\nError: Server Address has not yet been set and validated.")
        return ""
    #construct address
    requestAddress = baseAddress.replace("IP",address)
    print("Requesting from %s..." % (requestAddress))

    response = ""


    if authRequired:
        #if auth is required, pass request with already provided credentials
        response = requests.get(requestAddress,headers=HEADERS,verify=False,auth=(user,password))
    else:
        response = requests.get(requestAddress,headers=HEADERS,verify=False)

    data = ""
    if response:
        #parse the response as json
        data = json.loads(response.text)
    else:
        requestErrorMessages()
        sys.exit()

    return data




def requestErrorMessages():
    #Error message to be displayed when a page request fails
    print("\nThere was an error contacting the main page. Please ensure the following requirements are met:")
    print("\n~  You have a stable internet connection.")
    print("\n~  OpenVPN is connected and successfully authenticated.")
    print("\n~  The IP address provided is correct and the corresponding machine is online and has redfish installed.")
