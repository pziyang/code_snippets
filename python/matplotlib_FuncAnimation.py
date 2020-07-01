import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# generate 1 sine and cosine curve
x = np.arange(0.0, 2.0*np.pi, 0.001)
y = np.sin(x)
z = np.cos(x)

# generate frames data
frames = np.arange(0.0, 2.0*np.pi, 0.1)

# create figure and axis
fig, ax = plt.subplots()

# set axis explicitly
ax.set(xlim=[0, 2*np.pi], ylim=[-1,1])

# plot as line
ax.plot(x, y, 'r',
        x, z, 'b')

# get two 2DLine handle 
fh = ax.plot([], [], 'ro',
          [], [], 'bo')

# init function
def init():
    # set initial marker
    fh[0].set_data(0, 0)
    fh[1].set_data(0, 1)
    
    return fh

# animation function
def animate(i):
    fh[0].set_data(i, np.sin(i))
    fh[1].set_data(i, np.cos(i))
    
    return fh

"""
#=============================================================================
# for single line, use fh[0]

# plot as line
ax.plot(x, y, 'r')

# get two 2DLine handle 
fh = ax.plot([], [], 'ro')

# init function
def init():
    # set initial marker
    fh[0].set_data(0, np.sin(0))
    
    return fh

# animation function
def animate(i):
    fh[0].set_data(i, np.sin(i))
    
    return fh
#=============================================================================
"""

# create animation using the animate() function
myAnimation = animation.FuncAnimation(fig, animate, frames, init_func=init, \
                                      interval=10, blit=True, repeat=True)

plt.show()