from controller import Controller

import getpass

if 'Charl' == getpass.getuser():
    program = Controller()
else:
    print("You are not authorized to use this program.")
    exit()

