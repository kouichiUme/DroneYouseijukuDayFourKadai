from dronekit import connect, VehicleMode, Command,LocationGlobalRelative
from pymavlink import mavutil
import time
import sys

#
# tcp:127.0.0.1:5770
#  copter tcp:127.0.0.1:5763
#  rover1   tcp:127.0.0.1:5773
#  rover2   tcp:127.0.0.1:5783
#  boat1    tcp:127.0.0.1:5793
#  boat2   tcp:127.0.0.1:5803
#  boat1    tcp:127.0.0.1:5813
#  plane   tcp:127.0.0.1:5823

vehicle = connect('tcp:127.0.0.1:5773',wait_ready=True, timeout=60)


try:
    vehicle.wait_for_armable()
    vehicle.wait_for_mode("GUIDED")
    vehicle.arm()
    time.sleep(1)
    vehicle.wait_for_mode("TAKEOFF")
    #Home location set 
    point1 = LocationGlobalRelative(-35.878275,149.165218, 20)
    vehicle.simple_goto(point1)

    while(True):
        # river1 
        point2 = LocationGlobalRelative(35.87694326855309, 140.33935666245745)
        # river point 2
        # 35.87694326855309, 140.33935666245745
        # 35.86498250692829, 140.32039472643464 
        vehicle.simple_goto(point2)

        point3 = LocationGlobalRelative(35.86498250692829, 140.32039472643464)
        vehicle.simple_goto(point3)
        # 35.86484669941803, 140.30981619440792
        point4 = LocationGlobalRelative(35.86484669941803, 140.30981619440792)
        vehicle.simple_goto(point4)
        # 35.871108231642914, 140.29105598517782
        # 
        point5 = LocationGlobalRelative(35.86484669941803, 140.30981619440792)
        vehicle.simple_goto(point5)

        point4 = LocationGlobalRelative(35.86484669941803, 140.30981619440792)
        vehicle.simple_goto(point4)

        point3 = LocationGlobalRelative(35.86498250692829, 140.32039472643464)
        vehicle.simple_goto(point3)



except TimeoutError as takeoffError:
    print("Takeoff is timeout!!!")
    sys.exit()
