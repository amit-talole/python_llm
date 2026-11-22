
light = 'yellow  '

if(light.strip().lower() == 'green'):
    print('Go')
elif(light.strip().lower() == 'yellow'):
    print('Slow down')
else:
    print('Stop')