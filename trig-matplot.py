#
# Display trigonometric functions on a unit circle
# Adarsh Daheriya 2018-05-12
#

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure("Trigonometric Functions")

ax = fig.add_subplot(111)

# lock the aspect
ax.set_aspect(1)

# visible axes segment
xy_min = -3
xy_max = 3
ax.set_xlim(xy_min, xy_max)
ax.set_ylim(xy_min, xy_max)

#unit circle
t = np.arange(-5.0, 5.0, 0.01)
plt.plot(np.cos(t), np.sin(t), linewidth=1)

# axes
left,right = ax.get_xlim()
low,high = ax.get_ylim()
plt.arrow( 0, 0, right, 0,    length_includes_head = True, head_width = 0.05 )
plt.arrow( 0, 0, left,  0,    length_includes_head = True, head_width = 0.05 )
plt.arrow( 0, 0, 0,     high, length_includes_head = True, head_width = 0.05 ) 
plt.arrow( 0, 0, 0,     low,  length_includes_head = True, head_width = 0.05 ) 

# grid
plt.grid()

# draw line at given angle
x1 = 0
y1 = 0
angle = 30 # vary this to change angle
rad = np.radians(angle)

tan = np.tan(rad)
sin = np.sin(rad)
cos = np.cos(rad)
csc = 1/sin
sec = 1/cos
cot = 1/tan
x = np.array(range(-3,4))
y = tan*(x-x1) + y1
plt.plot(x,y, marker = ".", markevery = 1, markerfacecolor = "b")

# draw extended line, passing through [x1,y1] and [x2,y2]
def plot_segment(x1, y1, x2, y2, c):
    line_eqn = lambda x : ((y2-y1)/(x2-x1)) * (x - x1) + y1        
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
ax.annotate('sin', xy=(1, 1), xytext=(cos-0.25, sin-0.3), color = 'blue' )

#cos
Cos = patches.FancyArrowPatch([0, -0.2], [cos, -0.2], arrowstyle="]-[", color = "black")
ax.add_patch(Cos)
ax.annotate('cos', xy=(1, 1), xytext=(0.4, -0.15))

#tangent
Tangent = patches.FancyArrowPatch([sec, 0], [0, csc], arrowstyle="|-|", color = "red")
ax.add_patch(Tangent)
plt.annotate('tangent', xy=(1, 1), xytext=(1.3, -1), color = 'red')

#cosec
Csc = patches.FancyArrowPatch([-0.1, 0], [-0.1, csc], arrowstyle="]-[", color = "magenta")
ax.add_patch(Csc)
Csc = patches.FancyArrowPatch([-0.1, 0.05], [cot, 1.1], arrowstyle="]-[", color = "magenta")
ax.add_patch(Csc)
ax.annotate('csc', xy=(1, 1), xytext=(-0.4, 1), color = 'magenta')

#sec
Sec = patches.FancyArrowPatch([0, -0.3], [sec, -0.3], arrowstyle="]-[", color = "cyan")
ax.add_patch(Sec)
Sec = patches.FancyArrowPatch([0, 0.05], [1, tan+0.05], arrowstyle="]-[", color = "cyan")
ax.add_patch(Sec)
ax.annotate('sec', xy=(1, 1), xytext=(0.4, -0.45), color = 'cyan')

#tan
Tan = patches.FancyArrowPatch([1.03, 0], [1.03, tan], arrowstyle="]-[", color = "pink")
ax.add_patch(Tan)
ax.annotate('tan', xy=(1, 1), xytext=(cos+0.2, sin-0.35), color = 'pink')
Tan = patches.FancyArrowPatch([cos+0.03, sin+0.03], [sec+0.03, 0.03], arrowstyle="]-[", color = "pink")
ax.add_patch(Tan)

#cot
Cot = patches.FancyArrowPatch([0, 1.05], [cot, 1.05], arrowstyle="]-[", color = "green")
ax.add_patch(Cot)
Cot = patches.FancyArrowPatch([0.04, csc], [cos+0.04, sin], arrowstyle="]-[", color = "green")
ax.add_patch(Cot)
ax.annotate('cot', xy=(1, 1), xytext=(cot/2, 1.1), color = 'green')

plt.show()
