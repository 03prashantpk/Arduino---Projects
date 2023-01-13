import socket
import time
def ifConnected():
    IPaddress=socket.gethostbyname(socket.gethostname())
    if IPaddress=="127.0.0.1":
        # print("No internet, your localhost is "+ IPaddress)
        connection =  0
        return False

    else:
        # print("Connected, with the IP address: "+ IPaddress )
        connection = 1
        return True
