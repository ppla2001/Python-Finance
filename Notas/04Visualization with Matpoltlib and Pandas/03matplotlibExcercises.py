#%%
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2
# %%
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('Y')
ax.set_xlabel('X')
ax.set_title('Title')
ax.plot(x,y)
plt.show()
# %%
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax1.plot(x,y)
ax2 = fig.add_axes([0.2,0.5,.2,.2])
ax2.plot(x,y)
plt.show()
# %%
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])
ax.set_ylabel('Z')
ax.set_xlabel('X')
ax.plot(x,z)

ax2 = fig.add_axes([0.2,0.5,.4,.4])
ax2.set_ylabel('Y')
ax2.set_xlabel('X')
ax2.set_title('ZOOM')
ax2.set_xlim(20,22)
ax2.set_ylim(30,50)
ax2.plot(x,y)

plt.show()
# %%
fig,axes = plt.subplots(nrows=1,ncols=2)
axes[0].plot(x,y,lw=3,ls='--',color='red')
axes[1].plot(x,z,lw=3,ls='-',color='green')
# %%
