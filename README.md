# MagFish

## An interface between Redfish and MagDB

A python script designed to take a server's IP, MAC address and Rack Location in order to fetch all relevant metadata and commit the information to MagDB.
Requires the server to have Redfish installed, and for the client machine to have OpenVPN installed and connected to the correct domain, as well as possess the authenification credentials for the server.

Redfish: http://redfish.dmtf.org/
