python autocopter.py &
python drone_plane.py &
python drone_plane.py &


sim_vehicle.py -v Copter -L Kawachi -i 1
sim_vehicle.py -v Rover -L Kawachi -i 2
sim_vehicle.py -v Rover -L Kawachi -i 3
sim_vehicle.py -v Rover -L Kawachi --frame motorboat -i 4
sim_vehicle.py -v Rover -L Kawachi --frame motorboat -i 5
sim_vehicle.py -v Plane -L Kawachi -i 6
