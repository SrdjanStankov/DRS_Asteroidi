# Echo client program
import socket
import multiprocessing as mp
from time import sleep
# exPipes
class SocketSend(mp.Process):
    def __init__(self,pipe):
         super().__init__(target=self.Send, args=[pipe])
    
    
    HOST = 'localhost'  # The remote host
    PORT = 50055        # The same port as used by the server

   
    def Send(self,pipe):
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.HOST, self.PORT))
                    text2send = pipe.recv()
                    s.sendall(text2send.encode('utf8'))
            sleep(1 / 60)