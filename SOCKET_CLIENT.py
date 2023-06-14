#This script is for testing socket functionality locally
import socket

class SOCKET_CLIENT():
    
    def sendToServer(ID, DATA):
        HOST = "ec2-52-14-145-28.us-east-2.compute.amazonaws.com"  # The server's hostname or IP address
        PORT = 5353  # The port used by the server

        DATA = DATA * 100

        formatID = "ID:" + str(ID) + ","
        formatDATA = "DATA:" + str(DATA)

        IDToBytes = bytes(formatID, "utf-8")
        DATAToBytes = bytes(formatDATA, "utf-8")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("TRYING TO CONNECT: ", HOST, " : ", PORT)
            s.connect((HOST, PORT))
            print("CONNECTED TO SERVER")

            s.sendall(IDToBytes + DATAToBytes)
            print("DATA SENT")


ID = 360 # Unique Client ID
DATA = 531.89 # this number is the current power output
SOCKET_CLIENT.sendToServer(ID, DATA)