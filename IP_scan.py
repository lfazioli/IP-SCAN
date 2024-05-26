#Hello, this is a IP scan.
# We usa a normal comand arp -a and with this command we can scan our network
# this is a Simple script but is really useful if you are starting out in the world of hacking

#Author: Snorty :)
import pyfiglet  # is a Lybrary for the Text
import os # is a Library for use the command of bash


def main():  #Function main 
    Text = pyfiglet.figlet_format("IP SCAN") # Text
    print(Text)

# Decision

    print("Hello do you want Scan your network?")
    print("[1] Scan Network")
    print("[2]Exit\n") 

    Decision = str(input()) # I translate Decision in a string type 

# Condition
    if Decision == "1":
         print("\n")
         # Command for Scan network
         command = "arp -a"
         os.system(command)
    elif Decision == "2":
        exit
    else:
        print("\n")
        print("you should use 1 or 2 :)" )
        main()
main() #Start Program     

     




