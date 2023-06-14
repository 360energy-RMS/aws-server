import socket
import select

class SOCKET_SERVER:
    def startServer():
        HOST = "0.0.0.0"  #  Server any Address
        PORT = 5353  #  Port to listen on

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(10)
            s.setblocking(False)  #  Set the socket to non-blocking mode
            
            while True:
                ready_to_read, _, _ = select.select([s], [], [], 1)  #  Wait for 1 second
                if ready_to_read:  #  If there is a client ready to connect
                    conn, addr = s.accept()
                    with conn:
                        print("CONNECTED BY:", addr)

                        data = conn.recv(1024)

                        return data
