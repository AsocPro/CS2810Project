#!/usr/bin/env python 
 
import xmpp, serial, time

arduino = serial.Serial('/dev/ttyACM0',115200, timeout=1)
arduino.open() 
 
user="zpgibbs@gmail.com"
password=raw_input("Enter the password: ")
server="gmail.com"


def respond(dta):
#   if dta == "Light On":
#       msg = "Light On"
#       send = True
#   elif dta =="Light Off":
#       msg = "Light Off"
#       send = True
#   else:
    if dta is not None:
        msg = dta
        send = True
    else:
        msg = dta
        send = False
    messageSent = xmpp.Message("asocpro@gmail.com", msg)
    messageSent.setAttr('type', 'chat')
    if send:
        connection.send(messageSent)
        
        
def sendMessage(code):
    if code == "kiin":
        arduino.write("k")
    elif code == "L":
        arduino.write("L")
    elif code == 'l':
        arduino.write("l")
    else:
        arduino.write(" ")

def message_handler(connect_object, message_node): 
       messageCode = message_node.getBody()
       if(messageCode != None):
           print messageCode
           sendMessage(messageCode)


#      connect_object.send( xmpp.Message( message_node.getFrom() ,message)) 
 
jid = xmpp.JID(user) 
connection = xmpp.Client(server) 
connection.connect() 
result = connection.auth(jid.getNode(), password, "LFY-client") 
connection.RegisterHandler('message', message_handler) 
 
connection.sendInitPresence() 


try:



   while connection.Process(1): 
      # pass
       response = arduino.readline()
       print response
       respond(response)


except KeyboardInterrupt:
        arduino.close()



