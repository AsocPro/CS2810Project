#!/usr/bin/env python 
 
import xmpp, serial, time

arduino = serial.Serial('/dev/ttyACM0',115200, timeout=1)
arduino.open() 

def respond(dta):
    if dta == "Light On":
        msg = "Light On"
        send = True
    elif dta =="Light Off":
        msg = "Light Off"
        send = True
    else:
        msg = dta
        send = False
    messageSent = xmpp.Message("asocpro@gmail.com", msg)
    messageSent.setAttr('type', 'chat')
    if send:
        connection.send(messageSent)
 
user="zpgibbs@gmail.com"
password=raw_input("Enter the password: ")
server="gmail.com"
 
jid = xmpp.JID(user) 
connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "LFY-client") 
 
connection.sendInitPresence() 

arduino.write("1")
try:

   while True: 
       response = arduino.readline()
       print response
       respond(response)

except KeyboardInterrupt:
        arduino.close()

