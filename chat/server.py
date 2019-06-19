#!/usr/bin/env python

'''
############################
Copyright (C) 2018 Jean-Baptiste DURVILLE
This program is free software: you can redistribute it and/or modify
it under the terms of the
GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later
version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.\n\nYou should have received a copy
of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
############################
'''

from serverUtils import Server, Connection
import socket
import sys
import messageUtils as mu

###### GET IP ADDRESS AND PORT
if len(sys.argv)!=2:
    print("[ERROR] Expected one argument, got", len(sys.argv)-1)
    exit()

ipAddress = ""#"127.0.0.1"
try:
    port = int(sys.argv[1])
except:
    print("[ERROR] Wrong type for first arg, I was expecting a port number!")
    exit()

####### LAUNCH SERVER
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = Server(s, ipAddress, port, 3)

server.printChoice()

####### RECEIVE INCOMING CONNECTIONS
while server.connectionOn:
	conn, addrFrom = server.socketO.accept()
	print(conn)
	server.addConnection(conn, addrFrom)

exit()
	