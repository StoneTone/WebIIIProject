from phue import Bridge
import random as r
from time import sleep
from flask import Flask
from PIL import ImageColor
from flask import render_template, request
app = Flask(__name__)

"""Connecting to the bridge"""
bridge = Bridge("192.168.4.20")
bridge.connect()

"""
Getting the specific names for the lights without 
having to use the numbers
"""
lights = bridge.get_light_objects('name')

#lights
strip = lights["Light Strip"]
out = lights["Outside Light"]

"""setting up the server"""
@app.route("/", methods= ['GET', 'POST'])
def ButtonInput():
    if request.method == 'POST':
        if request.form.get('On'):
            strip.on = True
        if request.form.get('Off'):
            strip.on = False
    return render_template('app.html')

@app.route("/uInput", methods= ['GET', 'POST'])        
def uInput():
    if request.method == 'POST':
        if request.form.get('brightness'):
            brit = request.form['brightness']
            strip.brightness = int(brit)
        if request.form.get('color'):
            #red = pow((red + 0.055) / (1.0 + 0.055), 2.4) if red > 0.04045 else (red / 12.92)
            #green = pow((green + 0.055) / (1.0 + 0.055), 2.4) if green > 0.04045 else (green / 12.92)
            #blue =  pow((blue + 0.055) / (1.0 + 0.055), 2.4) if blue > 0.04045 else (blue / 12.92)
            color = request.form.get('color')
            RGB = ImageColor.getcolor(color, "RGB")
            
            
    
    return render_template('app.html')

if __name__ == "__main__":
    app.run()




"""
for x in range(100):
    lights["Light Strip"].hue = r.randint(1,16000)
    lights["Outside Light"].hue = r.randint(1,16000)
    sleep(1)
"""


    


