barts-linux-dashboard
=====================
The goal of this project is to create a dashboard to add users, groups, make sudoers entries, etc. across multiple machines.  It should be so easy that anyone can do it so I can focus on other things. The python code listed here is the my first try at anything python. My environment is as follows:

1) OS = CentOS release 6.5 (Final)
2) python = Python 3.4.1
4) bash = GNU bash, version 4.1.2(1)-release (x86_64-redhat-linux-gnu)

CHANGE LOG:

6/7/2014
1) Add in the menu() function, meny.py is now fixed to allow the following:
    - selection 1 will show the next GID and return to the menu
    - selection 2 will show the next UID and return to the menu
    - selection 3 will exit the python script entirely
    - any other selection will do nothing and kick back into the main menu/function

6/10/2014
1) Add in functions to handle each if/elif/else statement
    - the menu interface is exactly the same, no difference to the user
