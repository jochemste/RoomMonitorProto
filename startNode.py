from HardwareInterface import HardwareInterface
from UserInterface import UserInterface

def main():
    hardwareInterface = HardwareInterface()
    userInterface = UserInterface()

    try:
        while(1):
            data_dict = hardwareInterface.read()
            userInterface.provide(data_dict)
    except KeyboardInterrupt as e:
        userInterface.stop()
        print("")
        print("Exiting")

main()
