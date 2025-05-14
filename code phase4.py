import random
import time

grid_size = 5
grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

# Place 3 random waste locations marked with 'W'
waste_locations = random.sample([[x, y] for x in range(grid_size) for y in range(grid_size)], 3)
for x, y in waste_locations:
    grid[y][x] = 'W'

# Starting position of the robot
robot_pos = [0, 0]

def display_grid():
    for y in range(grid_size):
        for x in range(grid_size):
            if [x, y] == robot_pos:
                print('R', end=' ')
            else:
                print(grid[y][x], end=' ')
        print()
    print()

def move_robot():
    # Move towards closest waste
    min_dist = float('inf')
    target = None
    for wx, wy in waste_locations:
        dist = abs(robot_pos[0] - wx) + abs(robot_pos[1] - wy)
        if dist < min_dist:
            min_dist = dist
            target = [wx, wy]

    if target:
        if robot_pos[0] < target[0]:
            robot_pos[0] += 1
        elif robot_pos[0] > target[0]:
            robot_pos[0] -= 1
        elif robot_pos[1] < target[1]:
            robot_pos[1] += 1
        elif robot_pos[1] > target[1]:
            robot_pos[1] -= 1

        # Check if robot collected waste
        if robot_pos == target:
            print(f"Collected waste at {target}")
            grid[target[1]][target[0]] = '.'
            waste_locations.remove(tuple(target))

# Main loop
for _ in range(20):
    display_grid()
    if not waste_locations:
        print("All waste collected!")
        break
    move_robot()
    time.sleep(0.5)