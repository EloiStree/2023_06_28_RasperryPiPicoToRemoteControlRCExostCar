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

## Set the power of the remote control on at star
power_on_at_start=True

## Will trigger a while loop to run 8 9 10 11 pins in a loop
motor_debug_test=False

usePrintlog=True

# My relay is inversed
motorOn=False
motorOff=True

# The pin int id
leftForwardPin =8
leftBackwardPin =9
rightForwardPin =10
rightBackwardPin =11
powerOnOfPin=12

# The index of the pin in the array of Pin objects
leftForwardIndex =0
leftBackwardIndex =1
rightForwardIndex =2
rightBackwardIndex =3
powerOnOfIndex=4

## All the pin to use.
rc_car_pins = [

    leftForwardPin, # Left Forward
    leftBackwardPin, # Left Backward
    rightForwardPin,# right forward
    rightBackwardPin,# right backward
    powerOnOfPin, # turn on off the power
]
## All the pin objects of the RC car to control
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
        # Maybe
        #pin.value( state? motorOn : motoroff)
        
def set_pin_rccar_to(index ,state):
    rc_car_pins_created[index].value(not state)
        #pin.value( state? motorOn : motoroff)

def set_lf_rf_lb_rb(lf, rf, lb, rb):
    set_pin_rccar_to(leftForwardIndex, lf)
    set_pin_rccar_to(rightForwardIndex, rf)
    set_pin_rccar_to(leftBackwardIndex, lb)
    set_pin_rccar_to(rightBackwardIndex, rb)

def uartToAction(message):
    if usePrintlog:
        print("|"+message+"|")
    tokens = message.split(' ')
    
    for shortcut in tokens:
        shortcut = shortcut.strip().lower()
        if usePrintlog:
            print("#"+shortcut+"#")
        if "on" == shortcut  or "1" == shortcut  :
            set_pin_rccar_to(powerOnOfIndex, True)
            
        elif "off" == shortcut or "0" == shortcut :
            set_pin_rccar_to(powerOnOfIndex, False)
            
        elif "lf0" == shortcut :
            set_pin_rccar_to(leftForwardIndex, False)
        elif "rf0" == shortcut :
            set_pin_rccar_to(rightForwardIndex, False)
        elif "lb0" == shortcut :
            set_pin_rccar_to(leftBackwardIndex, False)
        elif "rb0" == shortcut : 
            set_pin_rccar_to(rightBackwardIndex, False)
            
        elif "lf1" ==shortcut :
            set_pin_rccar_to(leftForwardIndex, True)
        elif "rf1" ==shortcut :
            set_pin_rccar_to(rightForwardIndex, True)
        elif "lb1" ==shortcut :
            set_pin_rccar_to(leftBackwardIndex, True)
        elif "rb1" ==shortcut :
            set_pin_rccar_to(rightBackwardIndex, True)
        
        elif "stop" ==shortcut or "s" ==shortcut :
            set_lf_rf_lb_rb(0,0,0,0)
            
        elif "up" ==shortcut or "u"  ==shortcut :
            set_lf_rf_lb_rb(1,1,0,0)
        elif "down" ==shortcut or "d"  ==shortcut :
            set_lf_rf_lb_rb(0,0,1,1)
        elif "right" ==shortcut or "r"  ==shortcut :
            set_lf_rf_lb_rb(1,0,0,0)
        elif "left" ==shortcut or "l" ==shortcut :
            set_lf_rf_lb_rb(0,1,0,0)
        elif "fullright" ==shortcut or "fr" ==shortcut :
            set_lf_rf_lb_rb(1,0,0,1)
        elif "fullleft" ==shortcut or "fl" ==shortcut :
            set_lf_rf_lb_rb(0,1,1,0)


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