import socket
from threading import Thread

def listenConnection():
    bind_ip = input("Enter IP Address of this device: ")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((bind_ip, 9000))
    s.listen(1)
    conn, addr = s.accept()
    print('Sniffing time...')
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

if __name__ == '__main__':
    conn, addr, s = listenConnection()
    rcv = Thread(target=receiveMsg, args=(conn, ))
    rcv.start()
