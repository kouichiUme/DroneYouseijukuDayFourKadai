from dronekit import connect, VehicleMode, Command, LocationGlobalRelative
from pymavlink import mavutil
import time
import sys

vehicle = connect('tcp:127.0.0.1:5773',wait_ready=True, timeout=60)

#Home location set 
point1 = LocationGlobalRelative(35.878275,149.165218, 50)
vehicle.simple_goto(point1)


try:
    vehicle.wait_for_armable()
    vehicle.wait_for_mode("GUIDED")
    vehicle.arm()
    time.sleep(1)
    #take off
    vehicle.wait_simple_takeoff(50, timeout=60)

    while True:
        #neigber location set 
        point2 = LocationGlobalRelative(35.867003, 140.305987, 50)
        vehicle.simple_goto(point2)
        # Back to Home  idling time
        time.sleep(5)
        # Back to Home 
        vehicle.simple_goto(point1)
        time.sleep(5)

except TimeoutError as takeoffError:
    print("Takeoff is timeout!!!")
    sys.exit()
