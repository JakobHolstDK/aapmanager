#!/usr/bin/env python3
import sys
import requests

def main():
    # Define the inventory structure
    # Check for the command-line argument
    if len(sys.argv) != 2:
        print("Usage: {} --list".format(sys.argv[0]))
        sys.exit(1)

    # Respond to the --list command
    if sys.argv[1] == '--list':
        # the inventoty is at http://localhost:9990/inventory
        # read the inventory
        response = requests.get("http://localhost:9990/inventory")
        print(response.text)



    else:
        print("Invalid argument")
        sys.exit(1)

if __name__ == "__main__":
    main()
