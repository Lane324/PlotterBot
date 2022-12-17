# Pen Plotting G-code Generator

This code is designed to generated gcode of gemetrical shapes to be used with pen plotting robots

# Shapes

## Line

![Line](Images/line.png)

`line(start_point, end_point, x_coords, y_coords)`

## Hypocycloid

### Explaination:
![Hypocycloid](Images/hypocycloid.png)

### Examples:
`R=50, r=1.32, a=100`
![Example 1](Images/hypocycloid_ex1.png)

`R=50, r=1.32, a=50`
![Example 2](Images/hypocycloid_ex2.png)

`R=100, r=1.32, a=20`
![Example 3](Images/hypocycloid_ex3.png)


`hypocycloid(R, r, a ,theta ,resolution, x_coords, y_coords, x_shift=0, y_shift=0, send_to_plot=True, send_to_gcode=True)`


## Epicycloid

### Explaination:
![Epicycloid](Images/epicycloid.png)

### Examples:
`R=150, r=20, a=20`
![Example 1](Images/epicycloid_ex1.png)

`R=150, r=10, a=10`
![Example 2](Images/epicycloid_ex2.png)

`R=25, r=50, a=50`
![Example 3](Images/epicycloid_ex3.png)

`epicycloid(a, r, R, theta, resolution, x_coords, y_coords, x_shift=0, y_shift=0, send_to_plot=True, send_to_gcode=True)`

## Cycloid

### Explaination:
![Cycloid](Images/cycloid.png)

### Examples:
`R=5`
![Example 1](Images/cycloid_ex1.png)

`R=15`
![Example 2](Images/cycloid_ex2.png)

`R=25`
![Example 3](Images/cycloid_ex3.png)