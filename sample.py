# import asyncio
import time
from evdev import InputDevice, categorize, ecodes

source_device = None
target_device = None

# Init dev reference
while source_device is None and target_device is None:
  try:
    source_device = InputDevice('/dev/input/event1')
    target_device = InputDevice('/dev/hidg0')
  except Exception as err:
    print ("No device - waiting...")
    time.sleep (10)

# # Async helper 
# async def helper(source_device, target_device):
#   async for ev in source_device.async_read_loop():
#     print(categorize(ev))
#     target_device.write_event(ev)

# # Loop waiting for keystroke
# loop = asyncio.get_event_loop()
# loop.run_until_complete(helper(source_device, target_device))

for ev in source_device.async_read_loop():
  print(categorize(ev))
  target_device.write_event(ev)