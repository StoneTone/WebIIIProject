from phue import Bridge
import random as r
from time import sleep
from flask import Flask
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

strip = lights["Light Strip"]
out = lights["Outside Light"]

"""setting up the server"""
@app.route("/", methods= ['GET', 'POST'])
def button():
    if request.method == 'POST':
        if request.form.get('On'):
            strip.on = True
        if request.form.get('Off'):
            strip.on = False
        brit = request.form['Brightness']
        
    return render_template('app.html')
    
if __name__ == "__main__":
    app.run()




"""
for x in range(100):
    lights["Light Strip"].hue = r.randint(1,16000)
    lights["Outside Light"].hue = r.randint(1,16000)
    sleep(1)
"""


    


