import robot
r = robot.RobotController()
r.connect()

r.forward(350)
r.rotate_counterclockwise(90)
r.forward(100)
r.rotate_clockwise(90)
# Room 1 Code:
marker_1 = r.read_marker()
print(f"Marker Number: {marker_1}")
if marker_1 == 1:
    r.rotate_counterclockwise(90)
    r.forward(700)
    r.rotate_clockwise(90)
    t1 = r.take_temperature()
    print(f"Tempature in Room: {t1}")
    r.forward(110)
    person_1 = r.scan_for_people()
    print(f"Is a person there?: {person_1}")
    if person_1 == True:
        r.rescue_person()
        r.rotate_clockwise(180)
        r.forward(110)
        r.rotate_counterclockwise(90)
        r.forward(800)
        r.rotate_clockwise(90)
        r.forward(350)
        r.rotate_counterclockwise(180)
        r.forward(945)
        r.rotate_counterclockwise(90)
        r.forward(100)
        r.rotate_clockwise(90)
    if person_1 == False:
        r.rotate_clockwise(180)
        r.forward(110)
        r.rotate_counterclockwise(90)
        r.forward(700)
        r.rotate_counterclockwise(90)
        r.forward(615)
if marker_1 == 2:
    t1 = 0
    r.forward(600)
#Room 2 Code

temperature_list = [t1,]
print(f"Temperature List: {temperature_list}")
# End of Room 1. Amend temperature list later for other rooms.

