from HardwareInterface import HardwareInterface
from UserInterface import UserInterface

from os.path import exists
from os import remove

stop_file = "./stop"

class ServiceException(Exception):
    pass

def main():
    hardwareInterface = HardwareInterface()
    userInterface = UserInterface()

    try:
        while(1):
            data_dict = hardwareInterface.read()
            userInterface.provide(data_dict)
            if exists(stop_file):
                remove(stop_file)
                raise ServiceException
    except KeyboardInterrupt as e:
        userInterface.stop()
        print("")
        print("Exiting")
    except ServiceException as e:
        userInterface.stop()
        print("")
        print("Stopping service")

main()
