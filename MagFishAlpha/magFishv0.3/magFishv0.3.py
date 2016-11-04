
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
    import ssl
    import sys
    # Custom Imports
    import Machine #Machine class used to store the data
    import RequestURL #Contains functions for requesting from URL and error handling
    import ValidateIP #Function for validating whtether a string is a valid IPv4 or IPv6 address
    import AuthRedFish #Function for collecting and validating request credentials to the server
    import Addresses #Collection of constants for redfish address templates
    print("Done")
except Exception as error:
    print("Error")
    print("\nError: " + str(error))
    sys.exit()



#enter and validate the ip address of the server
address = "Failed"
while address == "Failed":
    address = ValidateIP.validate()

RequestURL.address = address

#request main redfish page as preliminary check for internet connection etc
redfishResponse = RequestURL.get(Addresses.MAIN_PAGE,False)
if (redfishResponse == "None"):
    sys.exit()

#print(redfishResponse)

print("\nConnection Established")

#once connection is Established
#validate authentification credentials by requesting a locked page until the request is accepted
credentials = AuthRedFish.authenticate(address)

while not credentials:
    credentials = AuthRedFish.authenticate(address)

RequestURL.user = credentials[0]
RequestURL.password = credentials[1]



print ("Creating machine object...",end="")
machine = Machine.Machine(address)
print("Done")

systemsAddress = Addresses.SYSTEM_PAGE.replace("IP",address)
response = RequestURL.get(Addresses.SYSTEM_PAGE,True)

print("\n")

machine.setManu(response["Manufacturer"])
machine.displayManu()

machine.setModel(response["Model"])
machine.displayModel()

machine.setPartNo(response["PartNumber"])
machine.displayPartNo()
