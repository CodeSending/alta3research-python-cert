#!/usr/bin/env python3

import netifaces

def returnip(adapter_name):
    return((adapter_name.ifaddresses[netifaces.AF_LINK])[0]['addr']) # returns the MAC

def returnmac(adapter_name):
    return((adapter_name.ifaddresses[netifaces.AF_INET])[0]['addr']) # returns the MAC

def main():
    for i in netifaces.interfaces():
        print('\n****** details of interface - ' + i + ' ******')
        try:
            print('MAC: ', end='') # This print statement will always print MAC without an end of line
            print(returnmac(netifaces.interfaces()) # Prints the MAC address
            print('IP: ', end='')  # This print statement will always print IP without an end of line
            
        except:          # This is a new line
            print('Could not collect adapter information') # Print an error message

main()
