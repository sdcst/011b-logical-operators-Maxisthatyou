#! python3
"""
Ask the user to enter a name. 
If the name is one of the names on a list of special users, greet them by name.
You will need to use a logical statement that checks to see if any of the names
matches the input name.  Don't be surprised if there are many and/or connectors.

(2 points) 

Inputs:
Name (string)

Outputs:
You are not a VIP.
Hi xxxxxx! You are a VIP!

Example:
Enter your name=>Gertrude
Hi Gertrude! You are a VIP!

Enter your name=>Gordon
You are not a VIP.
"""

VIPNames = ("Guile","Blanka","Christine","Carol","Richard","Daniel","Chun-Li")

x = str(input("Please enter your name> "))
x = x.strip()

if ("Guile" in x) or ("Blanka" in x) or ("Christine" in x) or ("Carol" in x) or ("Richard" in x) or ("Daniel" in x) or ("Chun-Li" in x):
    print(f"Hi {x}! You are a VIP!")
else:
    print(f"You are not a VIP.")