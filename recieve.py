#!/usr/bin/env python 
 
import xmpp, serial, time

arduino = serial.Serial('/dev/ttyACM1',115200, timeout=1)
arduino.open() 
 
user="zpgibbs@gmail.com"
password=raw_input("Enter the password: ")
server="gmail.com"
 

def message_handler(connect_object, message_node): 
       string messageCode = message_node.getBody()

#      connect_object.send( xmpp.Message( message_node.getFrom() ,message)) 
 
jid = xmpp.JID(user) 
connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "LFY-client") 
connection.RegisterHandler('message', message_handler) 
 
connection.sendInitPresence() 


try:



   while connection.Process(1): 
       pass

except KeyboardInterrupt:
        arduino.close()


def sendMessage(string code):
    if code == "":
        arduino.write("")
    elif code == "":
        arduino.write("")
