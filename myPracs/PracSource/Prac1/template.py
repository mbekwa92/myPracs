import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

global counter
counter = 0

def main():
    a = 0
    
    #setState(0,1,1)
    #pin      8 16 22
    #GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
    
    #while True:# Run forever
        
        #sleep(1)
        #GPIO.output(8, GPIO.HIGH)
        #sleep(1)
        #GPIO.output(8, GPIO.LOW)
        
        #sleep(1)
        #GPIO.output(16, GPIO.HIGH)
        #sleep(1)
        #GPIO.output(16, GPIO.LOW)
        
        #sleep(1)
        #GPIO.output(22, GPIO.HIGH)
        #sleep(1)
        #GPIO.output(22, GPIO.LOW)

def button_callback2(channel):
    #Decrement Interrupt Event handler
    
    
    global counter
    #sleep(1) sleep forfeited
    if counter == 0:
        counter = 7
    elif counter <= 7:    
        counter -=1
    
    state_of_leds = bin(counter)[2:].zfill(3)
    setState(state_of_leds[0],state_of_leds[1],state_of_leds[2])
    
    #Messages for the console and debbuggin purposes
    print(bin(counter)[2:].zfill(3),":",counter)
    print("Button Pressed")
    print(" ")

    
    

def button_callback(channel):
    
    #EventHandler for increment button -- called when the count up button is pushed 
    #logic for counter to allow wrap around when incrementing
    
    global counter
    if counter >= 7:
        counter = 0
    elif counter < 7:    
        counter +=1
    
    #represent the current count value as a 3 bit binary number
    state_of_leds = bin(counter)[2:].zfill(3)
    
    #use setState to output to the Led's
    setState(state_of_leds[0],state_of_leds[1],state_of_leds[2])
    
    #Increment Information to be printed to the console
    print(bin(counter)[2:].zfill(3),":",counter)
    print("Button Pressed")
    print(" ")
    

def setState(led0,led1,led2):
    """ 
       Method that extracts the bits from the 3 bit binary and set the correspondig led's state to
       the bit's value.
       ON = 1
       OFF = 0
       MSB = led0
       LSB = led2 
    
    """
    #Console purposes and debugging
    print(led0,led1,led2)
    
    
    if str(led0) == "1":
        #set High
        GPIO.output(8, GPIO.HIGH)
        
    else:
        #setlow
        GPIO.output(8, GPIO.LOW) # Turn off
        
    if str(led1) == "1":
        #set High
        GPIO.output(16, GPIO.HIGH) # Turn on
        
    else:
        #setlow
        GPIO.output(16, GPIO.LOW) # Turn off
        
    if str(led2) == "1":
        #set High
        GPIO.output(22, GPIO.HIGH) # Turn on
        
    else:
        #setlow
        GPIO.output(22, GPIO.LOW) # Turn off
        
    
         
        
if __name__=="__main__":
    #set up GPIOs -- initGPIOs and add event handlers for buttons
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(12, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
    GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
    GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback,bouncetime=300)
    GPIO.add_event_detect(12,GPIO.RISING,callback=button_callback2,bouncetime=300)
    
    while True:
        main()
    
GPIO.cleanup()
