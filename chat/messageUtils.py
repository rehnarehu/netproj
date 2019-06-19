def sendMsg(soc, msg):
    '''
    soc is the socket object called to send the message: soc.send(msg)
    username is the username of the user sending the msg
    msg is the msg to be send (w/ the \n at the end)
    '''
    #print('You: '+str(msg))
    soc.send(msg)

def askName():
    '''
    asks for username to be used when establishing connection with other peer
    '''
    username = raw_input("Please enter your username: ")
    print("Welcome "+str(username)+"!")
    return username
