python autocopter.py &
python drone_plane.py &

sim_vehicle.py -v Copter -L Kawachi -i 1
sim_vehicle.py -v Copter --map -i 2
sim_vehicle.py -v Rover -i 3
sim_vehicle.py -v Rover -L Kawachi --frame motorboat -i 4
