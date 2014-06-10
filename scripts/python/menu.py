#!/usr/local/bin/python3.4

## Imports
import sys
import subprocess

## menu function
def menu():
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
        gid()

    ## Print the next avaialbe UID
    elif selection == '2':
        uid()

    ## Exit the script
    elif selection == '3':
        exit()

    ## Tell the user to try again and kick back into the function
    else:
        print('Please try again')
        menu()

## GID function
def gid():
    print('The next GID is as follows')
    subprocess.call("/opt/admin-tools/scripts/bash/next-gid.sh", shell=True)
    menu()

## UID function
def uid():
    print('The next UID is as follows')
    subprocess.call("/opt/admin-tools/scripts/bash/next-uid.sh", shell=True)
    menu()

## exit function
def exit():
    print('Good bye')
    sys.exit()

menu()
