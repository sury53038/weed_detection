import RPi.GPIO as GPIO
import time

# Use BOARD numbering
GPIO.setmode(GPIO.BOARD)

# Define L298N input pins (BOARD pin numbering)
IN1 = 11  # Physical pin 11 (GPIO17)
IN2 = 12  # Physical pin 12 (GPIO18)
IN3 = 13  # Physical pin 13 (GPIO27)
IN4 = 15  # Physical pin 15 (GPIO22)

# Stepper Motor Full-Step Sequence
stepSequence = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

# Updated Steps per mm
steps_per_mm = 54.4  # Adjusted steps per mm

# Current position tracking
current_position = 0.0  # Initialize home position at 0 mm

# Set GPIO modes
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

def step_motor(step_count, delay_time, clockwise):
    """Moves the stepper motor a given number of steps"""
    for _ in range(step_count):
        for j in range(4):
            index = j if clockwise else (3 - j)
            GPIO.output(IN1, stepSequence[index][0])
            GPIO.output(IN2, stepSequence[index][1])
            GPIO.output(IN3, stepSequence[index][2])
            GPIO.output(IN4, stepSequence[index][3])
            time.sleep(delay_time / 1000.0)  # Convert ms to seconds

def move_to_position(target_position):
    """Moves the stepper motor to an absolute position"""
    global current_position
    distance = target_position - current_position  # Calculate required movement
    clockwise = distance > 0  # Determine direction
    steps = int(abs(distance * steps_per_mm))  # Convert mm to steps

    # Move stepper motor
    step_motor(steps, 2, clockwise)

    # Update current position
    current_position = target_position

try:
    print("System initialized at position 0 mm.")
    while True:
        pos_str = input("Enter position in mm: ")
        try:
            target_pos = float(pos_str)  # Convert input to float
            print(f"Moving to position: {target_pos} mm")
            move_to_position(target_pos)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

except KeyboardInterrupt:
    print("\nStopping and cleaning up GPIOs...")
    GPIO.cleanup()