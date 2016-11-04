class Machine:

    ip = ""

    manu = ""
    model = ""
    partNo = ""

    def __init__(self,ip):
        self.ip = ip

    def setManu(self,manu): self.manu = manu
    def getManu(self): return manu
    def displayManu(self): print("Manufacturer: " + self.manu)

    def setModel(self,model): self.model = model
    def getModel(self): return model
    def displayModel(self): print("Model: " + self.model)

    def setPartNo(self,partNo): self.partNo = partNo
    def getPartNo(self): return partNo
    def displayPartNo(self): print("Part Number: " + self.partNo)

def requestErrorMessages():
    #Error message to be displayed when a page request fails
    print("\nThere was an error contacting the main page. Please ensure the following requirements are met:")
    print("\n~  You have a stable internet connection.")
    print("\n~  OpenVPN is connected and successfully authenticated.")
    print("\n~  The IP address provided is correct and the corresponding machine is online and has redfish installed.")

#constructs and executes a request, based on the ip provided and whether authentification is required
#returns the response
def requestURL(baseAddress,authRequired):
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

print("\nInitialising...")
print("""
 _____         _____ _     _
|     |___ ___|   __|_|___| |_
| | | | .'| . |   __| |_ -|   |
|_|_|_|__,|_  |__|  |_|___|_|_|
          |___|
""")

print("Importing required packages...",end="")
try:
    import requests #main package for makiing get requests
    requests.packages.urllib3.disable_warnings()
    #Due to the nature of our systems, every request will print a warning about secuirty certificates to the terminal
    #This disables that
    from ipaddress import ip_address #used for ip address validation
    import ssl
    import json #used to parse the json response from redfish
    import sys
    import getpass #used for hidden password entry
    print("Done")
except Exception as error:
    print("Error")
    print("\nError: " + str(error))

# Collection of address templates
MAIN_PAGE = "https://IP/redfish/v1"
CHASSIS_PAGE = "https://IP/redfish/v1/Chassis"
SYSTEM_PAGE = "https://IP/redfish/v1/Chassis/System.Embedded.1"

#constant for head to be sent with each request
HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

#enter and validate the ip address of the server
verified = False
while not verified:
    print("\nPlease enter the IP address of the machine: ",end="")
    try:
        #attempt to convert the given ip to an ip address object
        address = str(ip_address(input("")))
        verified = True
        print("Address Accepted")
        #if not a valid ip, a value error is thrown
    except ValueError:
        print ("\nThe address provided is not a valid IPv4 or IPv6 address.")

#request main redfish page as preliminary check for internet connection etc
redfishResponse = requestURL(MAIN_PAGE,False)
if (redfishResponse == "None"):
    sys.exit()

#print(redfishResponse)

print("\nConnection Established")

authenticated = False
#once connection is Established
#validate authentification credentials by requesting a locked page until the request is accepted
while not authenticated:

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
        response = requests.get(authAddress,headers=HEADERS,verify=False,auth=(user,password))
        try:
            json_response = json.loads(response.text)
            print("Successful")
            authenticated = True
        except Exception:
            print("Failed")
            print("\nAre you sure you entered the correct user and password? Please try again.")
    except Exception as error:
        print(error)

print ("Creating machine object...",end="")
machine = Machine(address)
print("Done")

systemsAddress = SYSTEM_PAGE.replace("IP",address)
response = requestURL(SYSTEM_PAGE,True)

print("\n")

machine.setManu(response["Manufacturer"])
machine.displayManu()

machine.setModel(response["Model"])
machine.displayModel()

machine.setPartNo(response["PartNumber"])
machine.displayPartNo()
