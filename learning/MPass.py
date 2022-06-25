#   MPass.py    Password storage
'''
MASTER PASSWORD
Simple (unsecure) app to store passwords for different accounts,
used to copy and paste according to what's stored here
-
Extend: Copy to and from file - Add passwords - etc.
'''

import pyperclip

ALL = {
    'email':'somearbitraryvalueSAVED2022',
    'blog':'anythingTHATcantBEguessed2022-.',
    'bank':'NEVERstoreyourbankpassword2022...',
    'python':'snakesAREdangerous4U5!'
    }

#   GET the account for the password and copy to it clipboard

print('Which account would you like the password for')

#   (IF add a login for program then list accounts)

acc = input()

try:
    pw = ALL[acc]
    pyperclip.copy(pw)
    print('Password copied to clipboard')
except:
    print('Sorry. Do not have that password')

print('Press key..')
holder = input()

