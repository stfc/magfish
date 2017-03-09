try:
    import sys
    import requests #main package for http requests
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    import getpass
except ImportError as error:
    print("There was an error importing one or more of the modules. Are they named correctly?")
    print("\nError: " + str(error))
    sys.exit()
except Exception as error:
    print("An unknown exception occurred.")
    print("\nError: " + str(error))
    sys.exit()

#constant for head to be sent with each request
HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
#variable for ip address of machine
ADDRESS = ""

def authenticate(username):

    USER = username
    PASSWORD = ""

    while PASSWORD == "":
        PASSWORD = getpass.getpass(prompt="\nPlease enter the password for the server: ")

        authResponse = get("/redfish/v1/Systems/",True,USER,PASSWORD)

def requestErrorMessages():
    #Error message to be displayed when a page request fails
    print("\nThere was an error contacting the requested page. Please ensure the following requirements are met:")
    print("\n~  You have a stable internet connection.")
    print("\n~  OpenVPN is connected and successfully authenticated.")
    print("\n~  The IP address provided is correct and the corresponding machine is online and has RedFish installed.")
    print("\n~  The login credentials you provided are correct.")

def get(requestAddress,authRequired,USER,PASSWORD):
    requestAddress = "https://" + ADDRESS + requestAddress

    print("Requesting from %s..." % (requestAddress),end="")

    response = ""

    try:
        if authRequired:
            #if auth is required, pass request with already provided credentials
            response = requests.get(requestAddress,headers=HEADERS,verify=False,auth=(USER,PASSWORD))
        else:
            response = requests.get(requestAddress,headers=HEADERS,verify=False)
        print("Successful")
    except Exception as error:
        print("Error")
        requestErrorMessages()
        sys.exit()

    try:
        response = response.json()
    except Exception as error:
        requestErrorMessages()
        sys.exit()

    return response
