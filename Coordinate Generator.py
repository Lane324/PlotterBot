import math
import matplotlib.pyplot as plt
import Gcode_Generator

def line(start,end, x_coords, y_coords, send_to_plot=True, send_to_gcode=True):
    x=[start[0],end[0]]
    y=[start[1],end[1]]
    
    if send_to_plot == True:
        plot(x,y)
    
    if send_to_gcode == True:
        [x_coords, y_coords] = append_coords(x_coords, y_coords, x, y)

    return [x_coords, y_coords]   

def hypocycloid(R, r, a, theta, resolution, x_coords, y_coords, x_shift=0, y_shift=0, send_to_plot=True, send_to_gcode=True):
    x=[]
    y=[]
    i=0
    while i <= theta:
        x.append((R-r)*math.cos((r/R)*i)+a*math.cos((1-(r/R))*i)+x_shift)
        y.append((R-r)*math.sin((r/R)*i)-a*math.sin((1-(r/R))*i)+y_shift)
        i+=resolution
    
    if send_to_plot == True:
        plot(x,y)
    
    if send_to_gcode == True:
        [x_coords, y_coords] = append_coords(x_coords, y_coords, x, y)

    return [x_coords, y_coords]

def epicycloid(R, r, a, theta, resolution, x_coords, y_coords, x_shift=0, y_shift=0, send_to_plot=True, send_to_gcode=True):
    x=[]
    y=[]
    i=0
    while i < theta:
        x.append((R-r)*math.cos((r/R)*i)-a*math.cos((1-(r/R))*i)+x_shift)
        y.append((R-r)*math.sin((r/R)*i)-a*math.sin((1-(r/R))*i)+y_shift)
        i+=resolution
    
    if send_to_plot == True:
        plot(x,y)
    
    if send_to_gcode == True:
        [x_coords, y_coords] = append_coords(x_coords, y_coords, x, y)

    return [x_coords, y_coords]

def cycloid(R, theta, resolution, x_coords, y_coords, x_shift=0, y_shift=0, send_to_plot=True, send_to_gcode=True):
    x=[]
    y=[]
    i=0
    while i <= theta:
        x.append(R*(i-math.sin(i))+x_shift)
        y.append(R*(1-math.cos(i))+y_shift)
        i+=resolution
    
    if send_to_plot == True:
        plot(x,y)
    
    if send_to_gcode == True:
        [x_coords, y_coords] = append_coords(x_coords, y_coords, x, y)

    return [x_coords, y_coords]

def cardioid(r, c, theta, resolution, x_coords, y_coords, x_shift=0, y_shift=0, send_to_plot=True, send_to_gcode=True):
    x=[]
    y=[]
    i=0
    while i <= theta:
        r = 2*(1+c*math.cos(i))
        x.append(r*math.cos(i)+x_shift)
        y.append(r*math.sin(i)+y_shift)
        i+=resolution
    
    if send_to_plot == True:
        plot(x,y)
    
    if send_to_gcode == True:
        [x_coords, y_coords] = append_coords(x_coords, y_coords, x, y)

    return [x_coords, y_coords]

def other(r, c, theta, resolution, x_coords, y_coords, x_shift=0, y_shift=0, send_to_plot=True, send_to_gcode=True):
    x=[]
    y=[]
    i=0.1
    while i <= theta:
        r = math.log(i)
        x.append(r*math.cos(i)+x_shift)
        y.append(r*math.sin(i)+y_shift)
        i+=resolution
    
    if send_to_plot == True:
        plot(x,y)
    
    if send_to_gcode == True:
        [x_coords, y_coords] = append_coords(x_coords, y_coords, x, y)

    return [x_coords, y_coords]

def append_coords(x_old, y_old, x_new, y_new):
    x_old.append('BREAK1')
    y_old.append('BREAK1')
    for i in range(len(x_new)):
        if i == 1:
            x_old.append('BREAK2')
            y_old.append('BREAK2')
        x_old.append(float(f'{x_new[i]:.2f}'))
        y_old.append(float(f'{y_new[i]:.2f}'))

    return [x_old, y_old]

def plot(x,y):

    del_index = []
    for i in range(len(x)):
        if x[i] == 'BREAK1':
            del_index.append(i)
        if x[i] == 'BREAK2':
            del_index.append(i)

    c=0
    for i in del_index:
        del x[i-c]
        del y[i-c]
        c+=1

    plt.plot(x, y)
    plt.axis('square') 
    plt.xlim([150-215.9/2, 150+215.9/2])
    plt.ylim([150-279.4/2, 150+279.4/2])

x_coords = []
y_coords = []



[x,y] = line([50,20], [250,20], x_coords, y_coords)
[x,y] = line([250,20], [250,280], x_coords, y_coords)
[x,y] = line([250,280], [50,280], x_coords, y_coords)
[x,y] = line([50,280], [50,20], x_coords, y_coords)

# [x,y] = line([165,135], [165,165], x_coords, y_coords)
# [x,y] = line([165,165], [135,165], x_coords, y_coords)
# [x,y] = line([135,165], [135,135], x_coords, y_coords)
# [x,y] = line([135,135], [165,165], x_coords, y_coords)
# [x,y] = line([135,165], [165,135], x_coords, y_coords)


#  picture 1
# [x,y] = epicycloid(R=20, r=1, a=50, theta=41*math.pi, resolution=0.1, x_shift=150, y_shift=150, x_coords=x_coords, y_coords=y_coords)
# [x,y] = epicycloid(R=75, r=1, a=5, theta=151*math.pi, resolution=0.1, x_shift=150, y_shift=150, x_coords=x_coords, y_coords=y_coords)
# [x,y] = hypocycloid(R=90, r=1, a=10, theta=181*math.pi, resolution=0.1, x_shift=150, y_shift=150, x_coords=x_coords, y_coords=y_coords)
# [x,y] = hypocycloid(R=10, r=1, a=10, theta=20*math.pi, resolution=0.1, x_shift=150, y_shift=150, x_coords=x_coords, y_coords=y_coords)



gcode = Gcode_Generator.make_gcode(x_coords,y_coords,5000)

filename = "c:\\Users\\Lane\\Desktop\\test.gcode"

Gcode_Generator.save_gcode(filename, gcode)

plt.show()