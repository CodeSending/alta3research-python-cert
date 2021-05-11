#!/usr/bin/env python3                                                                 
ipchk = input("Apply an IP address: ") # this line now prompts the user for input      
ipcchk = ipchk.split(".")                                                              
                                                                                       
# if user set IP of gateway                                                            
#if ipchk == "192.168.70.1":                                                            
#   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")                                                                          
if len(ipcchk) != 4:
    for octect in ipcchk : 
        while True: 
            try: 
                if (int)(octect): 
                    IsNumerical = True 
                    print("This is a valid IP!"
                break 
            except ValueError: 
                print("This is not a valid IP!")
        
   #print("Not an IP Address")                                                          
                                         
                                        
                                           

