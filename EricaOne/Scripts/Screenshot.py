import mss
from screeninfo import get_monitors
from PIL import Image

# Get the list of monitors
monitors = get_monitors()

# Assuming the second monitor is the second in the list
second_monitor = monitors[1]

# Define the monitor area to capture
monitor_area = {
    "top": second_monitor.y,
    "left": second_monitor.x,
    "width": second_monitor.width,
    "height": second_monitor.height
}

# Capture the screenshot
with mss.mss() as sct:
    screenshot = sct.grab(monitor_area)

# Convert the screenshot to a PIL Image
img = Image.frombytes(
    'RGB',
    (screenshot.width, screenshot.height),
    screenshot.rgb
)

# Save the screenshot
img.save('second_monitor_screenshot.png')

print('Screenshot taken and saved as second_monitor_screenshot.png')

