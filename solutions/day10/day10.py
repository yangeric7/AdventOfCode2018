import parse
import numpy as np
import matplotlib.pyplot as plt 

input_string = '''position=<{x},{y}> velocity=<{dx},{dy}>'''

#boundary box where text could lie in. had to manually edit once it got close
x_boundry = 70
y_boundry = 10

def get_input():
    x = np.array([])
    y = np.array([])
    dx = np.array([])
    dy = np.array([])

    for i in open('input.txt'):
        point = parse.parse(input_string, i)

        x = np.append(x, int(point['x']))
        y = np.append(y, int(point['y']))
        dx = np.append(dx, int(point['dx']))
        dy = np.append(dy, int(point['dy']))

    return x, y, dx, dy
        
x, y, dx, dy = get_input()
close = False
time = 0
while not close:
    time += 1
    temp_x = x + dx*time
    temp_y = y + dy*time

    x_dist = max(temp_x) - min(temp_x)
    y_dist = max(temp_y) - min(temp_y)

    if x_dist < x_boundry and y_dist < y_boundry:
        close = True
        
print(time)

final_x = x + dx*time
final_y = y + dy*time

plt.plot(final_x, final_y, linestyle='None', marker='s')
plt.gca().invert_yaxis()
plt.show()
