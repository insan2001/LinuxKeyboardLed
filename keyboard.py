import os

led = 0
location = "/sys/class/leds/input4::scrolllock/brightness"

with open(location, "r") as f:
    data = f.read()

if(data=="1\n"):
    led = 0
else:
    led = 1

os.system(f"echo '{led}' | sudo tee {location}")
