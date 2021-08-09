import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01) # between 0.0 and 2.0 it's the interval and 0.01 is the step
print("No of elements = ",len(t), "\narray = ",t)
s = 1 + np.sin(2 * np.pi * t)
print(s)

fig, ax = plt.subplots() # we create the plot areas
ax.plot(t, s) # adds the two arrays to the plotting area ax - t hold the x values and s hold the y values

# set some labels for the plot
ax.set(xlabel = "time (s)", ylabel = "voltage (mV)", title = "About as simple as it gets")

ax.grid() # just adding grid, because why not
# we could also save figure as png
# fig.savefig("E:\Projects\python\python-programming\python-starter-kit\matplotlib\test.png") - this does not work for some reason

if __name__ == "__main__":
    mpl.use("qt5agg") # using qt5agg as backend driver for graphics
    plt.show()

