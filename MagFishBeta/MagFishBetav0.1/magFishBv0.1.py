print("Importing required packages...",end="")
try:
    import argparse #Used for parsing command line arguments
    import ipaddress
    import RequestURL
    print("Done")
except ImportError as error:
    print("There was an error importing one or more of the modules. Are they named correctly?")
    print("\nError: " + str(error))
    sys.exit()
except Exception as error:
    print("An unknown exception occurred.")
    print("\nError: " + str(error))
    sys.exit()

parser = argparse.ArgumentParser()
parser.add_argument("ip",help="The IP address of the server.",type=ipaddress.IPv4Address)
args = parser.parse_args()

print("""
 _____         _____ _     _
|     |___ ___|   __|_|___| |_
| | | | .'| . |   __| |_ -|   |
|_|_|_|__,|_  |__|  |_|___|_|_|
          |___|
""")

RequestURL.ADDRESS = str(args.ip)

print("Checking initial connection...")
testResponse = RequestURL.get("/redfish/v1",False,"","")

print("Authenitcating...")
RequestURL.authenticate()
