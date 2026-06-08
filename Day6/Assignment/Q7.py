#Create a traffic light system using match-case. Given a color ('red', 'yellow', 'green'), print the appropriate instruction. Add a guard condition in 'green' case: if speed > 60, print 'Slow down even on green'


color = input("Enter the color of the traffic light: ")
speed = int(input("Enter the speed of the vehicle: "))

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Slow down")
elif color == "green" and speed > 60:
    print("Slow down even on green")
elif color == "green":
    print("Go")
else:
    print("Invalid color")