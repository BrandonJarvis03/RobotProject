import robot
r = robot.RobotController()
r.connect()

r.forward(350)
r.rotate_counterclockwise(90)
r.forward(100)
r.rotate_clockwise(90)
# Room 1 Code:
m = r.read_marker()
print(f"Marker Number: {m}")
if m == 1:
    r.rotate_counterclockwise(90)
    r.forward(700)
    r.rotate_clockwise(90)
    t1 = r.take_temperature()
    print(f"Tempature in Room: {t1}")
    r.forward(110)
    n = r.scan_for_people()
    print(f"Is a person there?: {n}")
    if n == True:
        r.rescue_person()
        r.rotate_clockwise(180)
        r.forward(110)
        r.rotate_counterclockwise(90)
        r.forward(800)
        r.rotate_clockwise(90)
        r.forward(350)
        r.rotate_counterclockwise(180)
    if n == False:
        r.rotate_clockwise(180)
        r.forward(110)
        r.rotate_counterclockwise(90)
        r.forward(700)
        r.rotate_counterclockwise(90)
if m == 2:
    t1 = 0
temperature_list = [t1,]
print(f"Temperature List: {temperature_list}")
# End of Room 1. Amend temperature list later for other rooms.

