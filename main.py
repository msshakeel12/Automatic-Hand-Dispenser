#libraries for time delay and random functions 
import time
import random 



'''
function setup for the checking of the 
various componets used in the hardware 
and returns error accordingly, if no errors 
returns the intial light intensity of the room
'''
def setup():
    lcd_rgb(252,0,0)
    lcd_print("Hello")
    time.sleep(2)
    lcd_clear()
    lcd_print("setting up......")
    time.sleep(2)
    lcd_clear()
    lcd_print("..light sensor")
    x=analog_read(3)    
    #condition to check if the light sensor is plugged in 
    if x==None:
        return "error in light sensor"
    time.sleep(2)
    lcd_clear()
    lcd_print("..servo motor")
    y=digital_read(4)
    #condition to check if the servo motor is plugged in 
    if y==None:
        return "error in servo motor"
    time.sleep(2)
    #to set the servo to intial stage if the servo is not at 0
    servo_move(4,0)
    servo_move(4,180)
    time.sleep(2)
    servo_move(4,0)
    lcd_clear()    
    #returns the intial light intensity 
    return x


'''
function loop takes in the intial light 
intensity of the room as a parameter 
then loops and executes the output commands
if the intensity falls a particular value
or if the button is pressed.
'''
def loop(b):
    lcd_clear()
    y=digital_read(8)
    while(True):
        y=digital_read(8)
        x=analog_read(3)
        #executes the commands if the intensity decreases by 25 or if button is pressed 
        while(x<(b-25) or y==True):
	        servo_move(4,180)
	        time.sleep(1)
	        servo_move(4,0)
	        lcd_clear()
	        #z variable used for 20sec timer to wash hands 
	        z=0
	        while(z<20):
	            #the lcd changes the backlight every second for visualization of the timer
	            lcd_rgb(random.randint(200,255),random.randint(0,10),random.randint(0,250))
	            lcd_print(z+1)
	            z+=1
	            time.sleep(1)
	            lcd_clear()
                    
	        x=analog_read(3)
	        y=digital_read(8)
	        
    lcd_clear()
    lcd_rgb(0,255,0)

#b is for intial brightness of the room
b=setup()
#condition to check if b is integer to call the function loop 
if b.isdigit():
    loop(b)
#libraries for time delay and random functions 
import time
import random 



'''
function setup for the checking of the 
various componets used in the hardware 
and returns error accordingly, if no errors 
returns the intial light intensity of the room
'''
def setup():
    lcd_rgb(252,0,0)
    lcd_print("Hello")
    time.sleep(2)
    lcd_clear()
    lcd_print("setting up......")
    time.sleep(2)
    lcd_clear()
    lcd_print("..light sensor")
    x=analog_read(3)    
    #condition to check if the light sensor is plugged in 
    if x==None:
        return "error in light sensor"
    time.sleep(2)
    lcd_clear()
    lcd_print("..servo motor")
    y=digital_read(4)
    #condition to check if the servo motor is plugged in 
    if y==None:
        return "error in servo motor"
    time.sleep(2)
    #to set the servo to intial stage if the servo is not at 0
    servo_move(4,0)
    servo_move(4,180)
    time.sleep(2)
    servo_move(4,0)
    lcd_clear()    
    #returns the intial light intensity 
    return x


'''
function loop takes in the intial light 
intensity of the room as a parameter 
then loops and executes the output commands
if the intensity falls a particular value
or if the button is pressed.
'''
def loop(b):
    lcd_clear()
    y=digital_read(8)
    while(True):
        y=digital_read(8)
        x=analog_read(3)
        #executes the commands if the intensity decreases by 25 or if button is pressed 
        while(x<(b-25) or y==True):
	        servo_move(4,180)
	        time.sleep(1)
	        servo_move(4,0)
	        lcd_clear()
	        #z variable used for 20sec timer to wash hands 
	        z=0
	        while(z<20):
	            #the lcd changes the backlight every second for visualization of the timer
	            lcd_rgb(random.randint(200,255),random.randint(0,10),random.randint(0,250))
	            lcd_print(z+1)
	            z+=1
	            time.sleep(1)
	            lcd_clear()
                    
	        x=analog_read(3)
	        y=digital_read(8)
	        
    lcd_clear()
    lcd_rgb(0,255,0)

#b is for intial brightness of the room
b=setup()
#condition to check if b is integer to call the function loop 
if b.isdigit():
    loop(b)
