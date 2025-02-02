# Creates a function that accests sequences of words and numbers, split into parts and parsed it

class InvalidCommand(Exception):
    """Custom exception for invalid commands."""
    def __init__(self, message):
        super().__init__(f"Invalid command: {message}")


class LED:
    """A simple LED abstraction."""
    def __init__(self, ident):
        self.ident = ident
        self.intensity = 0
        self.color = (0, 0, 0)  # Default color (off)

    def set_brightness(self, ident, intensity):
        print(f"LED {ident} brightness set to {intensity}")
        self.intensity = intensity

    def set_color(self, ident, red, green, blue):
        print(f"LED {ident} color set to ({red}, {green}, {blue})")
        self.color = (red, green, blue)


class Robot:
    def __init__(self):
        self.leds = {i: LED(i) for i in range(5)}  # Example: 5 LEDs

    def beep(self, times, frequency):
        print(f"Beeping {times} times at {frequency}Hz")

    def rotate_neck(self, angle):
        print(f"Rotating neck to {angle} degrees")

    def handle_command(self, message):
        match message:
            case ["BEEPER", frequency, times]:
                self.beep(times, frequency)
            case ["NECK", angle]:
                self.rotate_neck(angle)
            case ["LED", ident, intensity]:
                self.leds[ident].set_brightness(ident, intensity)
            case ["LED", red, green, blue]:
                self.leds[0].set_color(0, red, green, blue)  # Assuming LED 0 for simplicity
            case _:
                raise InvalidCommand(message)


# Example usage
robot = Robot()
robot.handle_command(["BEEPER", 440, 3])
robot.handle_command(["NECK", 45])
robot.handle_command(["LED", 2, 75])
robot.handle_command(["LED", 255, 128, 64])  # Assuming default LED 0 for simplicity


