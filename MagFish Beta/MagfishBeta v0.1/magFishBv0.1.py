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
    import argparse #Used for parsing command line arguments
    import ValidateIP #Function for validating whtether a string is a valid IPv4 or IPv6 address
    import ipaddress
    print("Done")
except ImportError as error:
    print("There was an error importing one or more of the modules. Are they named correctly?")
    print("\nError: " + str(error))
    sys.exit()
except Exception as error:
    print("An unknown exception occurred.")
    print("\nError: " + str(error))
    sys.exit()

print("Parsing arguments...",end="")

parser = argparse.ArgumentParser()
parser.add_argument("ip",help="The IP address of the server.",type=ipaddress.IPv4Address)
args = parser.parse_args()

print("Done")
