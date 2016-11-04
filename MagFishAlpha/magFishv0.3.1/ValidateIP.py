from ipaddress import ip_address #used for ip address validation
def validate():
    print("\nPlease enter the IP address of the machine: ",end="")
    try:
        #attempt to convert the given ip to an ip address object
        address = str(ip_address(input("")))
        print("Address Accepted")
        return address
        #if not a valid ip, a value error is thrown
    except ValueError:
        print ("\nThe address provided is not a valid IPv4 or IPv6 address.")
        return "Failed"
    except Exception as error:
        print("An unknown exception has occurred.")
        print("\nError: " + error)
