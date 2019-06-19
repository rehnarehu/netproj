import messageUtils as mu
import time
from mythreads import Listener, Sender

class Client:
	'''
	Client represents one client connecting to a Server
	'''
	def __init__(self, socketO, ip, port, name):
		self.socketO = socketO
		self.ipAddress = ip
		self.port = port
		self.name = name
		self.connectionOn = False
		print("[INFO] connecting to: ("+self.ipAddress+", "+str(self.port)+")")
    		self.socketO.connect((self.ipAddress, self.port))
    		print("[SUCCESS] Connection established!")
    		self.connectionOn=True
		self.socketO.send(self.name+"\n")
		self.sender = Sender(self)
		self.listener = Listener(self.socketO, self)
		self.sender.start()
		self.listener.start()
                #time.sleep(1)
		print("[SUCCESS] Profile all set up!\n".format(self.name))

	def sendMessage(self, msg):
		mu.sendMsg(self.socketO, msg)
		if msg=="exit":
			self.close()

	def close(self):
		self.connectionOn = False
		self.socketO.close()
		print("[SUCCESS] Connection was closed, bye!")
		exit()

	def receivedMsg(self, conn, msg):
		if msg=="exit":
			self.close()
		print(msg)
