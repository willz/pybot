import threading
import ConfigParser
import Queue
from sockwrapper import SockWrapper
from parser import Parser

'''
'''
class MsgManager:
    def __init__(self):
        self.parser = Parser()
        self.recv_q = Queue.Queue()
        # create a socket object
        cf = ConfigParser.ConfigParser()
        cf.read('./client.conf')
        host = cf.get('socket', 'host')
        port = cf.getint('socket', 'port')
        self.sock = SockWrapper(host, port)
        # crete a receive thread
        self.recv_thread = threading.Thread(target = self.__recv)
        #self.recv_thread.daemon = True
        self.recv_thread.start()
        #self.recv_thread.join()

    def __del__(self):
        print 'end'
        

    def send(self, msg):
        if isinstance(msg, list):
            # input is a list, send messange one by one
            for cmd in msg:
                self.sock.send(cmd)
        else:
            self.sock.send(msg)

    # Get one info object from receive queue, if queue is empty,
    # this call will block
    def read(self):
        info = self.recv_q.get()
        return info

    def __recv(self):
        while True:
            msg = self.sock.recv()
            print msg
            info = self.parser.parse(msg)
            self.recv_q.put(info)
