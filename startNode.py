from HardwareInterface import HardwareInterface
from UserInterface import UserInterface

import time

def main():
    hardwareInterface = HardwareInterface()
    userInterface = UserInterface()

    try:
        while(1):
            data_dict = hardwareInterface.read()
            userInterface.provide(data_dict)
            time.sleep(1)
    except KeyboardInterrupt as e:
        userInterface.stop()
        print("")
        print("Exiting")

main()
