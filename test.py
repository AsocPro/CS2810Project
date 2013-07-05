import serial, time

arduino = serial.Serial('/dev/ttyACM0',115200, timeout=1)

arduino.open()

try:
	while True:
		arduino.write('p')
		response = arduino.readline()
		print response
		time.sleep(1)
		arduino.write('o')
		response = arduino.readline()
		print response
		time.sleep(1)
except KeyboardInterrupt:
	arduino.close()
