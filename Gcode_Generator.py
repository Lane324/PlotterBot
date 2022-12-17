def make_gcode(x,y,feed_rate):
    feed_rate_temp = 0

    gcode_prefix = ['G28', 'G1 Z52', 'G92 Z0', 'G90']
    gcode_suffix = []

    gcode = []


    for i in range(len(x)):

        if x[i] == 'BREAK1':
            command = 'LIFT'
            feed_rate_temp = 0

        elif x[i] == 'BREAK2':
            command = 'UNLIFT'
            feed_rate_temp = 0

        elif feed_rate_temp != feed_rate:
            command = f'G1 X{x[i]} Y{y[i]} F{feed_rate}'
            feed_rate_temp = feed_rate
            
        else:
            command = 'G1 X' + str(x[i]) + ' Y' + str(y[i])

        #print(command)
        
        gcode.append(command)
    gcode = gcode_prefix + gcode + gcode_suffix
    return gcode

def save_gcode(name,gcode):
    with open('%s' %name, 'w') as f:
        f.write('\n'.join(gcode))