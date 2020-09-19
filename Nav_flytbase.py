import time
from flyt_python import API
drone = API.navigation(timeout=120000)
time.sleep(3)
print("taking off upto 5m altitude")
drone.arm()
drone.take_off(5.0)
print("XYZ set points")
drone.position_set(6.5, 0, -5, relative=True)
drone.position_set(6.5, 6.5, -5, relative=True)
drone.position_set(0, 6.5, -5, relative=True)
drone.position_set(0, 0, -5, relative=True)

print("Landing now")
drone.land()
drone.disarm()

