from CopterThread import CopterThread
from BoatThread import BoatThread

def main():
        copter = CopterThread()
        copter.start()
        boat = BoatThread()
        boat.start()
main()