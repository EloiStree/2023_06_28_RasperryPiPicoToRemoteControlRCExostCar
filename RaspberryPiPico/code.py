import time
from machine import Pin
from machine import UART


##Full command line
#1 lf0 lb0 rf0 rb0; #All off except power
#1 lf1 lb1 rf1 rb1; #All on (means forward)
#1 lf1 lb0 rf0 rb0; #Turn forward left motor (means right)
#1 lf1 lb0 rf0 rb1; #Turn around very fast

uart = machine.UART(0, 9600)
uart.init(9600, bits=8, parity=None, stop=1)

power_on_at_start=True

motor_debug_test=False

motorOn=False
motorOff=True

leftForwardPin =8
leftBackwardPin =9
rightForwardPin =10
rightBackwardPin =11
powerOnOfPin=12

leftForwardIndex =0
leftBackwardIndex =1
rightForwardIndex =2
rightBackwardIndex =3
powerOnOfIndex=4


rc_car_pins = [

    leftForwardPin, # Left Forward
    leftBackwardPin, # Left Backward
    rightForwardPin,# right forward
    rightBackwardPin,# right backward
    powerOnOfPin, # turn on off the power
]
rc_car_pins_created= [
    
]





def initiate_rccarpin_as_out():
    for pin in rc_car_pins:
        pin = Pin(pin, Pin.OUT)
        pin.value(motorOff)
        rc_car_pins_created.append(pin)

def set_all_rccarpin_to(state):
    for pin in rc_car_pins_created:
        pin.value( not state)
        
def set_pin_rccar_to(index ,state):
    rc_car_pins_created[index].value(not state)
def set_pin_four_motor(leftForward, rightForward, ):
    rc_car_pins_created[index].value(not state)



def uartToAction(message):
    print("|"+message+"|")
    tokens = message.split(' ')
    
    for shortcut in tokens:
        shortcut = shortcut.strip().lower() 
        print("#"+shortcut+"#")
        if "on" in shortcut  or "1" == shortcut  :
            set_pin_rccar_to(powerOnOfIndex, True)
            
        elif "off" in shortcut or "0" == shortcut :
            set_pin_rccar_to(powerOnOfIndex, True)
            
        elif "lf0" in shortcut :
            set_pin_rccar_to(leftForwardIndex, False)
        elif "rf0" in shortcut :
            set_pin_rccar_to(rightForwardIndex, False)
        elif "lb0" in shortcut :
            set_pin_rccar_to(leftBackwardIndex, False)
        elif "rb0" in shortcut :
            set_pin_rccar_to(rightBackwardIndex, False)
            
        elif "lf1" in shortcut :
            set_pin_rccar_to(leftForwardIndex, True)
        elif "rf1" in shortcut :
            set_pin_rccar_to(rightForwardIndex, True)
        elif "lb1" in shortcut :
            set_pin_rccar_to(leftBackwardIndex, True)
        elif "rb1" in shortcut :
            set_pin_rccar_to(rightBackwardIndex, True)


print("Hello World")
initiate_rccarpin_as_out()
set_all_rccarpin_to(False)
if power_on_at_start:
    set_pin_rccar_to(powerOnOfIndex,True)

if motor_debug_test:
    time.sleep(1)
    set_all_rccarpin_to(False)
    time.sleep(1)
    set_all_rccarpin_to(True)
    time.sleep(1)
    set_all_rccarpin_to(False)
    time.sleep(1)



#SetAllToLow()

#leftForwardPin = Pin(8, Pin.OUT)
#leftForwardPin.low()

#leftBackwardPin = Pin(9, Pin.OUT)
#leftBackwardPin.low()

#rightForwardPin = Pin(10, Pin.OUT)
#rightForwardPin.low()

#rightBackwardPin = Pin(11, Pin.OUT)
#rightBackwardPin.low()

#powerOnOffPin = Pin(12, Pin.OUT)
#powerOnOffPin.hight()




if motor_debug_test:
    while True:
        if motor_debug_test:
            set_pin_rccar_to( leftForwardIndex  ,True)
            time.sleep(1)
            set_pin_rccar_to(leftForwardIndex ,False)
            time.sleep(1)
            set_pin_rccar_to(leftBackwardIndex ,True)
            time.sleep(1)
            set_pin_rccar_to(leftBackwardIndex ,False)
            time.sleep(1)
            set_pin_rccar_to(rightForwardIndex,True)
            time.sleep(1)
            set_pin_rccar_to(rightForwardIndex,False)
            time.sleep(1)
            set_pin_rccar_to(rightBackwardIndex,True)
            time.sleep(1)
            set_pin_rccar_to(rightBackwardIndex,False)
            time.sleep(1)
            
            

pin = Pin(26, Pin.OUT)
pin.value(True)
time.sleep(5);
pin.value(False)
            
line = b''  # Initialize an empty line buffer
data = ' '

while True:
    if uart.any():
        data = uart.read(1)  # Read one byte at a time        if data == b'\n':  # Check for newline character
        if  data == b'\n' or data == b';':
            line = line.decode('utf-8').strip().lower()  # Decode the received line
            uartToAction(line)
            line = b''  # Reset the line buffer
        else:
            line += data  # Append the received byte to the line buffer
    
    #print("On")
    # toggle the pin
    #p.high()
    #time.sleep(1);
    #print("Off")
    #p.low()
    #time.sleep(1);