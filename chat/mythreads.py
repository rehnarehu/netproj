import messageUtils as mu
import threading

class Listener(threading.Thread):
	def __init__(self, socketO, caller, connection=None):
		threading.Thread.__init__(self)
		self.caller = caller # Client or Server object
		self.connection = connection # Connection object or None if Client is calling this
		if self.connection==None: # caller is a Client
			self.check = self.caller
		else: # caller is a Server
			self.check = self.connection
		self.socketO = socketO # socket object
		print("[DEBUG] listener set up")

	def run(self):
		while self.check.connectionOn:
			received = self.socketO.recv(1024)
			if len(received)!=0:
				self.caller.receivedMsg(self.connection, received)
			received=""
		return

class Sender(threading.Thread):
	def __init__(self, caller):
		threading.Thread.__init__(self)
		self.caller = caller # Client or Server object
		print("[DEBUG] sender set up")

	def run(self):
		while self.caller.connectionOn:
			msg = raw_input()
			self.caller.sendMessage(msg)
		return
