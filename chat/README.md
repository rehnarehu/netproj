
This is a virtual chatroom, developed in python.

## Python app
Clients can connect to a server and communicate with each other.

The app uses `sockets` to establish the communication.

To launch the server (specify port number e.g. 55555):

```sh
./server.py 55555
```

To launch clients (specify server's IP address and port e.g. 127.0.0.1:55555):

```sh
./client.py 127.0.0.1 55555
```
