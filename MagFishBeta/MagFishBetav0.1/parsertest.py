import argparse
parser = argparse.ArgumentParser()
parser.add_argument("ip",help="The IP address of the server.")
args = parser.parse_args()
print(args.ip)
