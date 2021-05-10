#!/usr/bin/env python3

# create a list containing three items
my_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# display the first item in the list
#print("The first item in the list (IP): " + my_list[0] )

# display the second item in the list
#print("The second item in the list (port): " + str(my_list[1]) )

# display the third item in the list
#print("The last item in the list (state): " + my_list[2] )

print("IP Addresses", end=": ")
ip_only=[]

for value in my_list: 
   if("." in str(value)):
       ip_only.append = value
       print(value, end=' ')

print(ip_only)
    print("")
