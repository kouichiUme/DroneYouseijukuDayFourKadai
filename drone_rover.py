from dronekit import connect, VehicleMode, Command, LocationGlobalRelative
from pymavlink import mavutil
import time
import sys

vehicle1 = connect('tcp:127.0.0.1:5782',wait_ready=True, timeout=60)
vehicle2 = connect('tcp:127.0.0.1:5792',wait_ready=True, timeout=60)

try:
    vehicle1.wait_for_armable()
    vehicle1.wait_for_mode("GUIDED")
    vehicle1.arm()
    vehicle2.wait_for_armable()
    vehicle2.wait_for_mode("GUIDED")
    vehicle2.arm()
    # time.sleep(1)
    # vehicle.wait_simple_takeoff(10, timeout=20)
    # Home location set 
    point1 = LocationGlobalRelative(35.867003, 140.305987, 20)
    vehicle1.simple_goto(point1)

    #neigber location set 
    point2 = LocationGlobalRelative(35.877518, 140.295439, 20)
    vehicle1.simple_goto(point2)

    point3 = LocationGlobalRelative(35.879768, 140.348495, 20)
    vehicle2.simple_goto(point1)

    point4 = LocationGlobalRelative(35.876991, 140.348026, 20)
    vehicle2.simple_goto(point1)

except TimeoutError as takeoffError:
    print("Takeoff is timeou")
    sys.exit()
