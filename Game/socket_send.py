# Echo client program
import socket

class SocketSend:
    HOST = 'localhost'  # The remote host
    PORT = 50005        # The same port as used by the server
    def Send(self, text2send):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.HOST, self.PORT))
                s.sendall(text2send.encode('utf8'))
                text = ''
                while True:
                    bin = s.recv(1024)
                    text += str(bin, 'utf-8')
                    if not bin or len(bin) < 1024:
                        break
                print('Received', text)
