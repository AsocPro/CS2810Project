#!/usr/bin/env python 
 
import xmpp, serial, time

arduino = serial.Serial('/dev/ttyACM0',115200, timeout=1)
arduino.open() 
 
user="zpgibbs@gmail.com"
password=raw_input("Enter the password: ")
server="gmail.com"
 
jid = xmpp.JID(user) 
connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "LFY-client") 
 
connection.sendInitPresence() 

arduino.write("x")
try:

   while True: 
       response = arduino.readline()
       print response
       respond(response)

except KeyboardInterrupt:
        arduino.close()

def respond(string data):
    string msg
    if data == "":
        msg = ""
    elif data =="":
        msg = ""
    else:
        msg = "Unknown Query"
    messageSent = xmpp.Message("asocpro@gmail.com", msg)
    messageSent.setAttr('type', 'chat')
    connection.send(messageSent)
