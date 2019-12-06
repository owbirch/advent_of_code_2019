#Advent of code 2019: Day 2

f = open("day_3.txt", "r")
wire_1, wire_2 = f.read().strip().split('\n')
wire_1, wire_2 = [x.split(',') for x in [wire_1,wire_2]]

#PART 1
def get_points(wire):
    x = 0
    y = 0
    positions = {}
    step_count = 0
    for command in wire:
        direction = command[0]
        steps = int(command[1:])
        if direction == 'L':
            for step in range(steps):
                x += -1
                y += 0
                step_count += 1
                if (x,y) not in positions:
                    positions[(x,y)] = step_count
                    
        if direction == 'R':
            for step in range(steps):
                x += 1
                y += 0
                step_count += 1
                if (x,y) not in positions:
                    positions[(x,y)] = step_count
                    
        if direction == 'U':
            for step in range(steps):
                x += 0
                y += 1
                step_count += 1
                if (x,y) not in positions:
                    positions[(x,y)] = step_count
                    
        if direction == 'D':
            for step in range(steps):
                x += 0
                y += -1
                step_count += 1
                if (x,y) not in positions:
                    positions[(x,y)] = step_count
                    
    return positions

points_w1 = get_points(wire_1)
points_w2 = get_points(wire_2)
shared_points = set(points_w1.keys()).intersection(set(points_w2.keys()))
print(min(abs(x) + abs(y) for (x,y) in shared_points))
print(min(points_w1[i] + points_w2[i] for i in shared_points))