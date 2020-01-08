# Echo server program
import socket
import multiprocessing as mp
from time import sleep

class SocketListen(mp.Process):
    def __init__(self,pipe):
        super().__init__(target=self.Listen, args=[pipe])

    HOST = ''       # Symbolic name meaning all available interfaces
    PORT = 50055    # Arbitrary non-privileged port

    def Listen(self,pipe):
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.HOST, self.PORT))
                s.listen(1)
                conn, addr = s.accept()
                with conn:
                    text = ''
                    while True:
                        bin = conn.recv(1024)
                        text += str(bin, 'utf8')
                        if not bin or len(bin) < 1024:
                            break

                    pipe.send(text)

            sleep(1/60)
