#!/usr/bin/env python3o
import crayons
import time
import yaml
import urllib.request

"""Alta3 Research || Author: RZFeeser@alta3.com"""

def getyaml(yamlurl):
    with urllib.request.urlopen(yamlurl) as response:
        return yaml.load(response.read())

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd['todo']:
        print('Handshaking. .. ... connecting with ' + (crayons.yellow(coffeetime['ipaddr'])))
        time.sleep(2)
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd['todo']:
            print(crayons.green('    Attempting to send command --> ') + (crayons.red(mycmds['name'])) + " " + crayons.yellow(mycmds['state']) )
            time.sleep(1)
            # we'll learn to write code that sends cmds to device here
    print("\n")

def devicereboot(newwork):
    for ip in newwork['todo']:
        print('   Connecting to..' + (crayons.yellow(ip['ipaddr'])))
    print((crayons.red('\n     REBOOTING')),end='')
    time.sleep(1)
    print(" . ", end='', flush=True)
    time.sleep(3)
    print(" . ", end='', flush=True)
    time.sleep(3)
    print(" . ", end='', flush=True)
    print("NOW!")
    time.sleep(3)
# start our main script
def main():
    yamlurl='https://labs.alta3.com/courses/pyb/work2do-two'
    work2do = getyaml(yamlurl)   

    #work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    #["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    print("Welcome to the network device command pusher") # welcome message

    ## get data set
    print(crayons.green("\nData set found!!\n")) # replace with function call that reads in data from file
    time.sleep(3)

    ## run
    commandpush(work2do) # call function to push commands to devices
    devicereboot(work2do)

# call our main function
main()

