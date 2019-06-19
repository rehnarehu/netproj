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

import socket
import sys
import messageUtils as mu
from clientUtils import Client

if len(sys.argv)!=3:
    print("[ERROR] Expected 2 args, got",len(sys.argv)-1)
    exit()

ipAddress = sys.argv[1]
port = int(sys.argv[2])
myName = mu.askName()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client = Client(s, ipAddress, port, myName)
i=0
client.sendMessage("hello from "+myName + "\n\n")

while client.connectionOn:
	pass
	#print(client.connectionOn)
	#print(i)
	#i+=1;
print("out")
quit()
