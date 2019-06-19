import messageUtils as mu
import time
from mythreads import Listener, Sender

class Server:
	'''
	Server manages different clients, broadcasts message received from one user to the others
	'''
	def __init__(self, socketO, ip, port, incomingConnNbr):
		self.connectionOn = True
		self.socketO = socketO
		self.ipAddress = ip
		self.port = port
		self.connMaxNbr = incomingConnNbr
		self.connections=[]
		self.socketO.bind((self.ipAddress, self.port))
		self.socketO.listen(self.connMaxNbr)
		self.sender = Sender(self)
		self.sender.start()
		print('[INFO] listening on port: {}\n\n'.format(self.port))

	def getUsernames(self):
		res = []
		for client in self.connections:
			res.append(client.username)
		return res

	def addConnection(self, conn, addrFrom):
		newConn = Connection(self, conn, addrFrom)
		time.sleep(1)
                self.connections.append(newConn)
                self._broadcast("Server: {} just CONNECTED to the chat!\n\n".format(self.connections[-1].username))

	def receivedMsg(self, conn, msg):
		print("{}: {}".format(conn.username, msg))
		if msg=="exit":
			conn._close()
			self.connections.remove(conn)
			self._broadcast("Server: {} LEFT the chat!\n".format(conn.username))
		else:
			self._broadcast("{}: {}".format(conn.username, msg))

	def sendMessage(self, msg):
		if msg=="exit":
			self._broadcast("Server is shutting off, bye!\n\n")
			self._broadcast("exit")
                        connections = list(self.connections)
			for client in connections:
				client._close()
                                self.connections.remove(client)
			self.connectionOn = False
			exit()
		else:
			self._broadcast("Server: "+msg)

	def _broadcast(self, msg):
		for client in self.connections:
			client.sendMsg(msg)

	def findConnection(self):
		return self.connections
	def printChoice(self):
		self._broadcast("Do you want to join chat?")



class Connection:
	'''
	A Connection corresponds to a client connected to the Server.
	It has as attributes its associated Server, its own Socket object with its IP and port number.
	Each client is also asked a username to communicate with the others.
	'''
	def __init__(self, s, c, address):
		self.connectionOn = True
		self.server = s # server object
		self.clientConn = c # socket object
		self.clientIP = address[0]
		self.clientPort = address[1]
		self.username = self._initUsername() #self.clientConn.recv(1024)[:-1]
		self.listener = Listener(self.clientConn, self.server, self) ## testing
		self.listener.start()
		self.sendUsers()
		print("[CONNECTION] NEW connection: {} at {}:{}\n\n".format(self.username, self.clientIP, self.clientPort))

	def sendUsers(self):
		usersList = [username for username in self.server.getUsernames()]
                self.sendMsg("Welcome! Here are the users connected to the server: {}\n\n".format(usersList))

	def sendMsg(self, msg):
		try:
			print("[MESSAGE] sending msg to {} at {}:{}\n\n".format(self.username, self.clientIP, self.clientPort))
		except:
			print("[MESSAGE] sending msg to user at {}:{}\n\n{}".format(self.clientIP, self.clientPort, msg[:-1]))
		self.clientConn.send(msg)

	def _initUsername(self):
		username = self.clientConn.recv(1024)[:-1]
		if len(self.server.connections)==0: return username
		while username in self.server.getUsernames():
			self.sendMsg("Username already used by someone else, please get another one:")
			username = self.clientConn.recv(1024)
		return username

	def _close(self):
		self.connectionOn = False
		print("[CONNECTION] CLOSING connection: {} at {}:{}\n\n".format(self.username, self.clientIP, self.clientPort))
		self.clientConn.close()


