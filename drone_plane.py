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
    vehicle.wait_simple_takeoff(10, timeout=20)
    #Home location set 
    point1 = LocationGlobalRelative(-35.878275,149.165218, 20)
    vehicle.simple_goto(point1)

    #neigber location set 
    point2 = LocationGlobalRelative(35.867003, 140.305987, 20)
    vehicle.simple_goto(point2)

except TimeoutError as takeoffError:
    print("Takeoff is timeout!!!")
    sys.exit()
