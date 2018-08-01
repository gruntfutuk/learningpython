#! /usr/bin/env python3
# pw.py - An insecure password locker program.
import sys
import pyperclip

passwords = {'email': 'ASDLnlksnfqw9j',
             'blog': 'QJDLKCMoq9e0vmw',
             'luggage': '20KFM2MF9J2FMERFkwe'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy  account  password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the    account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + 'has been copied to clipboard')
else:
    print('There is no account named ' + account)
