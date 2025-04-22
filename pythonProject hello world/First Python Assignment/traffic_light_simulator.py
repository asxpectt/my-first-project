"""Traffic Light Simulator
Write a program that simulates a traffic light. It should:

Ask the user to input the current color of the traffic light (red, yellow, or green).

Print the corresponding action:

Red: "Stop"

Yellow: "Slow down"

Green: "Go"

Challenge: Add a condition to check if the input color is valid (red, yellow, or green). If not, print "Invalid color."


"""

# Ask user to input traffic light color
# if color chosen is red Print: "Stop"
# if color chosen is yellow Print : "Slow down"
# if color chosen is  Green print: "Go"
# Check if the input color is valid or invalid

traffic_light_color = input("What is the traffic light color? :")
if traffic_light_color == "red":
    print("Stop")
elif traffic_light_color == "yellow":
    print("Slow down")
elif traffic_light_color == "green":
    print("go")
else:
    print("Invalid color")
