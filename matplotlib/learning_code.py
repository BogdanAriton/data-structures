import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

"""
    A helper function to make a graph
    Parameters
    ----------
    ax : Axes - The axes to draw to
    data1 : array - The x data
    data2 : array - The y data
    param_dict : dict - Dictionary of kwargs to pass to ax.plot
    Returns
    -------
    out : list - list of artists added
"""
def my_plotter(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') - draw 4 dots at x,y coordinates
# plt.axis([0, 6, 0, 20])

# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)

# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')

if __name__ == "__main__":
    mpl.use("qt5agg") # using qt as backend driver for graphics
    plt.show()
