import time
from flyt_python import api
drone = api.navigation()
time.sleep(3)
print("Move in traj_square with side = 6.5 ")
drone.arm()
drone.take_off(5.0)
print("XYZ set points")
drone.set_local_position(6.5, 0, 0, body_frame=True)
drone.set_local_position(0, 6.5, 0, body_frame=True)
drone.set_local_position(-6.5, 0, 0, body_frame=True)
drone.set_local_position(0, -6.5, 0, body_frame=True)

print("Landing now")
drone.land()
drone.disarm()

