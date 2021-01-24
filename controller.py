from evdev import*

gamepad = InputDevice('/dev/input/event4')

print(gamepad)

buttons = {
    308: "Y",
    305: "B",
    304: "A",
    307: "X",
    311: "RB",
    310: "LB",
    172: "Xbox",
    158: "View",
    315: "Menu",
    318: "Joy1 clicked",
    318: "Joy2 clicked"
}

lt = 10
rt = 9

joy1_y = 1
joy1_x = 0
joy1_position = [0, 0]

joy2_y = 5
joy2_x = 2
joy2_position = [0, 0]

directionnal_button_x = 16
directionnal_button_y = 17

holded_button = 0

for event in gamepad.read_loop():
    #BUTTON
    if event.type == ecodes.EV_KEY: 
        val = int(event.value)

        if val == 1:
            print(buttons[int(event.code)] + " pressed")
        elif val == 0:
            print(buttons[int(event.code)] + " released")
        else:
            print("else")
            print(buttons[int(event.code)] + " value: " + str(event.value))

    #JOYSTICK
    elif event.type == ecodes.EV_ABS: 
        # JOY 1
        if event.code == joy1_x:
            joy1_position[0] = int(event.value)
            print("JOY 1: X " + str(joy1_position[0]) + " Y " + str(joy1_position[1]))

        elif event.code == joy1_y: 
            joy1_position[1] = int(event.value)
            print("JOY 1: X " + str(joy1_position[0]) + " Y " + str(joy1_position[1]))

        # JOY 2
        elif event.code == joy2_x:
            joy2_position[0] = int(event.value)
            print("JOY 2: X " + str(joy2_position[0]) + " Y " + str(joy2_position[1]))

        if event.code == joy2_y: 
            joy2_position[1] = int(event.value)
            print("JOY 2: X " + str(joy2_position[0]) + " Y " + str(joy2_position[1]))

        # DIRECTIONAL BUTTON AXIS Y
        elif event.code == directionnal_button_y:  
            pos = int(str(event.value).replace("L", ""))
            if pos > 0:
                print("Down pressed")
                holded_button = "Down"
            elif pos < 0:
                print("Up pressed")
                holded_button = "Up"
            elif pos == 0:
                print(holded_button + " released")

        # DIRECTIONAL BUTTON AXIS X
        elif event.code == directionnal_button_x:
            pos = int(str(event.value).replace("L", ""))
            if pos > 0:
                print("Right pressed")
                holded_button = "Right"
            elif pos < 0:
                print("Left pressed")
                holded_button = "Left"
            elif pos == 0:
                print(holded_button + " released")

        elif event.code == lt:
            print("LT pressed at " + str(event.value))
        
        elif event.code == rt:
            print("RT pressed at " + str(event.value))
    