print("Importing required packages...",end="")
try:
    import sys
    import argparse #Used for parsing command line arguments
    import ipaddress
    import RequestURL
    from Machine import Machine
    from Interface import Interface
    import RedfishAddresses
    print("Done")
except ImportError as error:
    print("There was an error importing one or more of the modules. Are they named correctly?")
    print("\nError: " + str(error))
    sys.exit()
except Exception as error:
    print("An unknown exception occurred.")
    print("\nError: " + str(error))
    sys.exit()

def chooseMainInterface(interfaces) :
    displayAllInterfaces(interfaces)

    newMachine.mac = ""

    while newMachine.mac == "":
        try:
            newMachine.mac = interfaces[int(input("\nPlease enter the ID of the main interface:"))].mac
        except:
            print("Invalid ID.")


    print("\nMain Interface Address set to: " + newMachine.mac)

def displayAllInterfaces(interfaces):
    print("\nInterfaces:")
    print("===========")
    for interface in interfaces:
        interface.displayAll()

parser = argparse.ArgumentParser()
parser.add_argument("ip",help="The IP address of the server.",type=ipaddress.IPv4Address)
parser.add_argument("fqdn",help="The chosen Fully Qualified Domain Name for the server.")
parser.add_argument("rack_id",help="The ID of the rack the machine is installed in.",type=int)
parser.add_argument("rack_row",help="The lowest row of the rack the machine is installed in.",type=int)
parser.add_argument("machine_size",help="The height of the machine in rows.",type=int)
parser.add_argument("username",help="The username for the server.")
args = parser.parse_args()

newMachine = Machine(str(args.ip))
newMachine.rack = str(args.rack_id)
newMachine.position = str(args.rack_row)
newMachine.units = str(args.machine_size)

print("""
 _____         _____ _     _
|     |___ ___|   __|_|___| |_
| | | | .'| . |   __| |_ -|   |
|_|_|_|__,|_  |__|  |_|___|_|_|
          |___|
""")

RequestURL.ADDRESS = newMachine.ip

print("Checking Initial Connection and Authenticating...")
RequestURL.USER = args.username
RequestURL.PASSWORD = RequestURL.requestPassword()
RequestURL.authenticate(args.username)
newMachine.fqdn = args.fqdn

print("Gathering main systems information...")
mainSystems = RequestURL.get(RedfishAddresses.MAIN_SYSTEM_PAGE,True)
print("Setting basic information...",end="")
newMachine.manufact = mainSystems[RedfishAddresses.MANU]
newMachine.model = mainSystems[RedfishAddresses.MODEL]
newMachine.serialNo = mainSystems[RedfishAddresses.SERIAL_NO]
print("Done")
print("Retrieving system memory information...",end="")
newMachineMemory = mainSystems[RedfishAddresses.MEMORY_DATA]
newMachine.totalMemory = int(newMachineMemory[RedfishAddresses.TOTAL_MEMORY])
print("Done")
print("Getting core details...",end="")
newMachineCores = mainSystems[RedfishAddresses.CORES_DATA]
newMachine.coreModel = newMachineCores[RedfishAddresses.CORE_MODEL]
newMachine.coreCount = int(newMachineCores[RedfishAddresses.CORE_COUNT])
print("Done")
print("Collecting network interfaces...")
networkInterfaces = RequestURL.get(RedfishAddresses.INTERFACES_PAGE,True)[RedfishAddresses.MEMBERS]
newMachineInterfaces = []

for interface in networkInterfaces:

    interfaceData = RequestURL.get(interface[RedfishAddresses.DATA_ID],True)
    status = interfaceData[RedfishAddresses.STATUS][RedfishAddresses.STATE]
    active = False

    if status == RedfishAddresses.ENABLED:
        active = True

    newInterface = Interface((len(newMachineInterfaces) + 1),interfaceData[RedfishAddresses.PERMANENT_MAC_ADDRESS],active,status)

    if newInterface.active:

        if newMachine.mac == "":

            print("Interface is enabled. Setting as main machine interface.")
            newMachine.mac = newInterface.mac

        else:

            print("Interface is active, but main interface is already set.")
    newMachineInterfaces.append(newInterface)

if newMachine.mac == "":
    print("\nNo network interfaces were active.")
    chooseMainInterface(newMachineInterfaces)

newMachine.displayAll()
displayAllInterfaces(newMachineInterfaces)
