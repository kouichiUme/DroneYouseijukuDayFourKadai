from dronekit import LocationGlobalRelative, VehicleMode, connect,time

# vehicle = connect('127.0.0.1:14551', wait_ready=True, timeout=60)
vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True, timeout=60)
print("Basic pre-arm checks")
# Don't let the user try to arm until autopilot is ready
while not vehicle.is_armable:
    print(" Waiting for vehicle to initialise...")
    time.sleep(1)

        
print("Arming motors")
# Copter should arm in GUIDED mode
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True

while not vehicle.armed:      
    print(" Waiting for arming...")
    time.sleep(1)

# モードはGUIDED
vehicle.mode = VehicleMode("GUIDED")

# 目標の緯度・経度、高度を設定する
# https://maps.gsi.go.jp/#8/-35.3574950/149.1701826/&base=std&ls=std&disp=1&vs=c1j0h0k0l0u0t0z0r0s0m0f1
aLocation = LocationGlobalRelative(35.879768, 140.348495, 20)

# simple_gotoを実行する
# vehicle.simple_goto(aLocation, groundspeed=1000, airspeed=


