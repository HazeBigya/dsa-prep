def car_fleet(position, speed, target):
    stack = []
    cars = list(zip(position, speed))
    cars.sort(reverse = True)
    for pos, spd in cars:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)
    return len(stack)

target = 12
position = [10, 8, 0, 5, 3]
speed    = [ 2, 4, 1, 1, 3]

print("The number of fleet are: ", car_fleet(position, speed, target))