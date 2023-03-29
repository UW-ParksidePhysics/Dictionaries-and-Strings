import numpy as np
import matplotlib.pyplot as plt
from numpy import exp, sin, pi
from matplotlib.animation import FuncAnimation
from IPython.display import HTML


# Define the wave packet function
def wave_packet(x, t):
   return np.exp(-(x - 3 * t) ** 2) * np.sin(3 * np.pi * (x - t))


# Define the x and time arrays for plotting the wave packet
xlist = np.linspace(-4, 4, 1001)
time_list = [-0.85, 0, 0.85]

# Create a list to store the generated figures
fig_list = []

# Loop through the time list and generate a figure for each time value
for time in time_list:
   ylist = wave_packet(xlist, time)
   fig = plt.figure()
   plt.plot(xlist, ylist)
   plt.xlabel('x')
   plt.ylabel('Amplitude')
   plt.title('One dimensional wave packet: t = %.2f s' % time)
   fig_list.append(fig)

# Create an animation of the wave packet
distance = np.linspace(-6, 6, 250)
times = np.linspace(-1,1, 250)
amplitude = exp(-(distance-3*times)**2) * sin(3*pi*((distance-3*times)))

fig = plt.figure()
lines = plt.plot(distance, times)
plt.axis([distance[0], distance[-1], -1,1])
plt.xlabel('Linear Distance')
plt.ylabel('Amplitude')

def frame(time):
  y = exp(-(distance-3*time)**2) * sin(3*pi*((distance-3*time)))
  lines[0].set_ydata(y)
  return lines

anim = FuncAnimation(fig, frame, frames = times*5, interval = 50)
anim_list = [anim]

# Create the HTML report
report = "<html><body>"

# Add the wave packet figures to the report
for fig in fig_list:
    plt.close(fig)  # Close the figure so it's not displayed twice
    report += "<h2>Wave packet plot</h2>"
    report += f"<div>{fig.canvas.to_html()}</div>"

# Add the wave packet animation to the report
report += "<h2>Wave animation</h2>"
report += f"<div>{anim.to_html()}</div>"

report += "</body></html>"

# Display the HTML report
HTML(report)
