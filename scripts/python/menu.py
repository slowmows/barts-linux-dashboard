#!/usr/local/bin/python3.4
import subprocess
## Ask the user to make a selection
print("Please choose your task from the menu")
## Print the menu
print("""
        1 - Show next available GID
        2 - Show next available UID
        3 - Exit
        """)

## Ask for a selection
selection = (input("Please make a selection from the menu: "))

## Print the next available GID
if selection == '1':
    print('The next GID is as follows')
    subprocess.call("/opt/admin-tools/scripts/bash/next-gid.sh", shell=True)

## Print the next avaialbe UID
elif selection == '2':
    print('The next UID is as follows')
    subprocess.call("/opt/admin-tools/scripts/bash/next-uid.sh", shell=True)

## Exit the script
elif selection == '3':
    print('Good bye')

## This should kick you back into the menu to make another selection
## not sure how to do this yet
else:
    print('Please try again')
