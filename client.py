import socket
from threading import Thread                    # For both sending and receiving messages

def receiveMsg(conn):                           # Copied from server.py
    global run
    while run:
        try:
            data = conn.recv(1024)
            if not data:
                continue
            print('\nMessage Received: {}'.format(data.decode()))

        except socket.error as msg:
            run = False
        except KeyboardInterrupt:
            run = False

    conn.close()

target_ip = input("Enter IP Address of server: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_ip, 8000))
run = True

rcv = Thread(target=receiveMsg, args=(s,))      # Thread for recieving messages
rcv.start()                                     # Start the receiving thread

while run:
    try:
        msg = input("Type Message: ")
        s.sendall(msg.encode())
    except socket.error as err:
        run = False
    except KeyboardInterrupt:
        run = False

s.close()
