import pyfirmata2

comport = 'COM3'
board = pyfirmata2.Arduino(comport)

# Define the pins for the LEDs
led_1 = board.get_pin('d:8:o')
led_2 = board.get_pin('d:9:o')
led_3 = board.get_pin('d:10:o')
led_4 = board.get_pin('d:11:o')
led_5 = board.get_pin('d:12:o')

def led(fingerUp):
    # Control each LED individually based on fingerUp input
    if fingerUp[0] == 1:
        led_1.write(1)  # Turn LED 1 on
    else:
        led_1.write(0)  # Turn LED 1 off
    
    if fingerUp[1] == 1:
        led_2.write(1)  # Turn LED 2 on
    else:
        led_2.write(0)  # Turn LED 2 off
    
    if fingerUp[2] == 1:
        led_3.write(1)  # Turn LED 3 on
    else:
        led_3.write(0)  # Turn LED 3 off
    
    if fingerUp[3] == 1:
        led_4.write(1)  # Turn LED 4 on
    else:
        led_4.write(0)  # Turn LED 4 off
    
    if fingerUp[4] == 1:
        led_5.write(1)  # Turn LED 5 on
    else:
        led_5.write(0)  # Turn LED 5 off

