def move_forward():
    print("Moving forward...")

def stop():
    print("Stopping...")

def turn_right():
    print("Turning right...")

def detect_waste():
    return True

def send_data(load_level, battery_level, location):
    print(f"Sending data: Load={load_level}, Battery={battery_level}, Location={location}")

def main():
    for i in range(3):
        dist = 25
        if dist < 20:
            stop()
            turn_right()
        else:
            move_forward()
            detect_waste()
            stop()
            print("Waste detected! Operating arm...")
            send_data(50, 80, "12.9716, 77.5946")

main()