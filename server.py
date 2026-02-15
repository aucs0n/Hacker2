import socket
from threading import Thread

run = True

def listenConnection():
    bind_ip = input("Enter IP Address of this server: ")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((bind_ip, 8000))
    s.listen(1)
    conn, addr = s.accept()
    print('Server accepted client connection...')
    return conn, addr, s

def receiveMsg(conn):
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

if __name__ == '__main__':
    print("run 'ipconfig' (windows) or 'ip a' (linux) for IP address of machine.\n\n")
    print("Hi! Im Server :)\n\n")
        
    conn, addr, s = listenConnection()
    rcv = Thread(target=receiveMsg, args=(conn, ))
    rcv.start()

    while run:
        try:
            msg = input("Type Message: ")
            conn.sendall(msg.encode())
        except socket.error:
            run = False
        except KeyboardInterrupt:
            run = False
    
    s.close()
