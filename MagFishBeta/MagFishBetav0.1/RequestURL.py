try:
    import requests #main package for http requests
    import sys
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
#variables for auth credentials
USER = ""
PASSWORD = ""

def requestErrorMessages():
    #Error message to be displayed when a page request fails
    print("\nThere was an error contacting the requested page. Please ensure the following requirements are met:")
    print("\n~  You have a stable internet connection.")
    print("\n~  OpenVPN is connected and successfully authenticated.")
    print("\n~  The IP address provided is correct and the corresponding machine is online and has redfish installed.")
