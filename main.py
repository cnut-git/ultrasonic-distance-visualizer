import serial
import time

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation


PORT = "COM4"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=0.01)
time.sleep(2)

current_value = 0
plt.style.use('default')
plt.rcParams['figure.figsize'] = (4, 3)
plt.rcParams['font.size'] = 12

fig, ax = plt.subplots()
ax.axis([0, 70, 0, 70])
ax.set_xlabel('')
ax.set_ylabel('Distance')
rect = patches.Rectangle(
            (0, current_value),     
            70, 10,                
            facecolor = '#ab3844',
            fill=True,
        )
box = ax.add_patch(rect)

dis_text = ax.text(35, 35, '', color='r', ha='center', va='center', fontweight='bold')
value_text = ax.text(35, 60, f'{current_value}cm', color='black', ha='center', va='center', fontweight='bold')

def update(frame):
    global current_value

    while ser.in_waiting:
        raw = ser.readline().decode(errors="ignore").strip()
        try:
            v = int(raw)
        except ValueError:
            continue
        if v != 0:
            current_value = v
        else:
            if current_value<10:
                current_value = v

    value_text.set_text(f"Distance: {current_value} cm")
    box.set_y(current_value)
    if current_value <= 10:
        dis_text.set_visible(True)
    else:
        dis_text.set_visible(False)

    return value_text,


def on_close(event):
    ser.close()


fig.canvas.mpl_connect("close_event", on_close)

ani = FuncAnimation(fig, update, interval=30, blit=False)
plt.show()