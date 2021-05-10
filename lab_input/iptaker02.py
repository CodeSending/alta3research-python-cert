#!/usr/bin/env python3
user_input = input("Please enter an IPv4 IP address:")
vendor_name = input("What is the vendor name:")

## the line below creates a single string that is passed to print()
# print("You told me the IPv4 address is:" + user_input)

## print() can be given a series of objects separated by a comma
print("You told me the IPv4 address is:", user_input)
print("You told me the vendor is:", vendor_name)

