#
# Display trigonometric functions on a unit circle
# Adarsh Daheriya 2018-05-12
#

import numpy              as np
import matplotlib.pyplot  as plt
import matplotlib.patches as patches

fig = plt.figure ("Trigonometric Functions")

ax = fig.add_subplot (111)

# lock the aspect
ax.set_aspect (1)

# visible axes segment
xy_min = -3
xy_max = 3
ax.set_xlim (xy_min, xy_max)
ax.set_ylim (xy_min, xy_max)

# axes
left, right = ax.get_xlim()
low, high   = ax.get_ylim()
plt.arrow( 0, 0, right, 0,    length_includes_head = True, head_width = 0.05 )
plt.arrow( 0, 0, left,  0,    length_includes_head = True, head_width = 0.05 )
plt.arrow( 0, 0, 0,     high, length_includes_head = True, head_width = 0.05 ) 
plt.arrow( 0, 0, 0,     low,  length_includes_head = True, head_width = 0.05 ) 

# grid
plt.grid()

# draw line at given angle
# vary this to change angle
angle = 30

rad = np.radians(angle)

tan = np.tan(rad)
sin = np.sin(rad)
cos = np.cos(rad)
csc = 1/sin
sec = 1/cos
cot = 1/tan

def draw_angle_line(dx, dy, rad):
    x = np.array (range (-3, 4))
    y = tan * (x - dx) + dy
    plt.plot (x, y, marker = ".", markevery = 1, markerfacecolor = "b")

draw_angle_line(0, 0, rad)

# plot circle
t = np.arange (-5.0, 5.0, 0.01)
def plot_circle (x, y, c):
    plt.plot (x, y, color = c, linewidth=1)

# unit circle
plot_circle (np.cos(t), np.sin(t), "black")

# 'tan' circle
plot_circle (np.sqrt (1 + tan**2) * np.cos(t), np.sqrt (1 + tan**2) * np.sin(t), "pink")

# 'cot' circle
plot_circle (np.sqrt (cot**2 + 1) * np.cos(t), np.sqrt (cot**2 + 1) * np.sin(t), "green")

# draw extended line, passing through [x1,y1] and [x2,y2]
def plot_segment(x1, y1, x2, y2, c):
    line_eqn = lambda x : ( (y2 - y1) / (x2 - x1) ) * (x - x1) + y1        
    xrange = np.arange(-2, 2, 0.1)
    plt.plot(xrange, [ line_eqn(x) for x in xrange], color=c, linestyle='-.', linewidth=0.2)

plot_segment(10,  sin,        -10,        sin,        "blue")    # sin intercept
plot_segment(cos, 10,         cos+0.0001, -10,        "black")   # cos intercept
plot_segment(10,  tan,        -10,        tan,        "pink")    # tan intercept
plot_segment(cot, 1,          cot+0.0001, -1,         "green")   # cot intercept
plot_segment(1,   csc+0.0090, -1,         csc+0.0091, "magenta") # csc intercept
plot_segment(sec, 1,          sec+0.0001, -1,         "cyan")    # sec intercept
plot_segment(sec, 0, 0,       csc,                    "red")     # tangent line

#sin
Sin = patches.FancyArrowPatch([cos, 0], [cos, sin], arrowstyle="]-[", color = "blue")
ax.add_patch(Sin)
ax.annotate('sin', xy=(1, 1), xytext=(cos-0.35, (sin/2)-0.1), color = 'blue' )

#cos
Cos = patches.FancyArrowPatch([0, -0.2], [cos, -0.2], arrowstyle="]-[", color = "black")
ax.add_patch(Cos)
ax.annotate('cos', xy=(1, 1), xytext=((cos/2)-0.1, -0.15))

#tangent
Tangent = patches.FancyArrowPatch([sec, 0], [0, csc], arrowstyle="|-|", color = "red")
ax.add_patch(Tangent)
plt.annotate('tangent', xy=(1, 1), xytext=(1.3, -1), color = 'red')

#cosec
Csc = patches.FancyArrowPatch([-0.1, 0], [-0.1, csc], arrowstyle="]-[", color = "magenta")
ax.add_patch(Csc)
Csc = patches.FancyArrowPatch([-0.1, 0.05], [cot, 1.1], arrowstyle="]-[", color = "magenta")
ax.add_patch(Csc)
ax.annotate('csc', xy=(1, 1), xytext=(-0.4, csc/2), color = 'magenta')

#sec
Sec = patches.FancyArrowPatch([0, -0.3], [sec, -0.3], arrowstyle="]-[", color = "cyan")
ax.add_patch(Sec)
Sec = patches.FancyArrowPatch([0, 0.05], [1, tan+0.05], arrowstyle="]-[", color = "cyan")
ax.add_patch(Sec)
ax.annotate('sec', xy=(1, 1), xytext=(0.4, -0.45), color = 'cyan')

#tan
Tan = patches.FancyArrowPatch([1.03, 0], [1.03, tan], arrowstyle="]-[", color = "pink")
ax.add_patch(Tan)
ax.annotate('tan', xy=(1, 1), xytext=(1.1, tan/2), color = 'pink')
Tan = patches.FancyArrowPatch([cos+0.03, sin+0.03], [sec+0.03, 0.03], arrowstyle="]-[", color = "pink")
ax.add_patch(Tan)

#cot
Cot = patches.FancyArrowPatch([0, 1.05], [cot, 1.05], arrowstyle="]-[", color = "green")
ax.add_patch(Cot)
Cot = patches.FancyArrowPatch([0.04, csc], [cos+0.04, sin], arrowstyle="]-[", color = "green")
ax.add_patch(Cot)
ax.annotate('cot', xy=(1, 1), xytext=(cot/2, 1.1), color = 'green')

plt.show()
