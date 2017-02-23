print("Importing required packages...",end="")
try:
    import sys
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
parser.add_argument("rack_id",help="The ID of the rack the machine is installed in.",type=int)
parser.add_argument("rack_row",help="The lowest row of the rack the machine is installed in.",type=int)
parser.add_argument("machine_size",help="The height of the machine in rows.",type=int)
parser.add_argument("username",help="The username for the server.")
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

print("Authenticating...")
RequestURL.authenticate(args.username)
