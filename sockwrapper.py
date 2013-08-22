from socket import *
import ConfigParser

class SockWrapper:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket(AF_INET, SOCK_DGRAM)

    def send(self, msg):
        self.sock.sendto(msg, (self.host, self.port))

    def recv(self, bufsize = 8192):
        data, addr = self.sock.recvfrom(bufsize)
        return data


