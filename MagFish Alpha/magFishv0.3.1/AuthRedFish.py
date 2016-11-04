import getpass #used for hidden password entry
import requests #main package for making get requests
import json #used to parse the json response from redfish
import sys
from time import sleep
from Addresses import CHASSIS_PAGE #Collection of constants for redfish address templates
requests.packages.urllib3.disable_warnings()
#Due to the nature of our systems, every request will print a warning about security certificates to the terminal
#This disables the warnings from printing to cmmndline at every request

#constant for head to be sent with each request
HEADERS = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

def authenticate(address,failed):

    user = ""
    password = ""

    while user == "":
        user = input("\nPlease enter the user name for the server: ")
    while password == "":
        #takes input without displaying characters for more secure password entry
        password = getpass.getpass("\nPlease enter the password for the server: ")
    #construct address for chassis page based on ip address
    authAddress = CHASSIS_PAGE.replace("IP",address)

    if failed:
        print("\n")
        waiting("Server lockout due to incorrect login attempt. Waiting 60 seconds...",30,1)

    print("\nAuthenticating...",end="")


    timedOut = True
    while timedOut:
        try:
            response = requests.get(authAddress,headers=HEADERS,verify=False,auth=(user,password))
            timedOut = False
        except TimeoutError:
            print("Request from server timed out. Retrying...",end="")
        except Exception as error:
            print("An unknown exception occured.")
            print("\nError: " + str(error))
            print("\n" + str(type(error)))
            sys.exit()

    if not response:
        print("Access denied. \nAre you sure your credentials were entered correctly? Please try again.")
        authenticate(address,True)

    credentials = [user,password]
    return credentials

    print("Success")

def waiting(message,time,interval):

    spinner = ["|","/","-","\\"]
    spin = 0
    if time % interval == 0:
        steps = int(time / interval)

        for i in range (0, steps + 1):
            printstring = message + "|"
            for x in range (0,steps - i):
                printstring += "■"
            printstring += spinner[spin]
            if spin == 3:
                spin = 0
            else:
                spin += 1
            for y in range(0,i):
                printstring += " "
            printstring += "|"



            print(printstring,end='\r',flush=True)
            sleep(interval)
    else:
        print("Error: Time and Interval must be dividable.")
        print("Waiting specified time.")
        sleep(time)
