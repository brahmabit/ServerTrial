import socket
import threading
import sys
import FileManager


class CLient:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def sendMsg(self):
        while True:
            #input("")
            imageName = input("")
            #imageEncoded = FileManager.sendImage(imageName)
            self.sock.send(FileManager.sendImage(imageName))
            #self.sock.send(imageName.encode)

    def __init__(self, address):
        self.sock.connect((address, 8080))

        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()

        while True:
            data =self.sock.recv(5000000)
            if not data:
                print("Server did not reply")
                break
            print(str(data, 'utf-8'))

if(len(sys.argv)>1):
    client = CLient(sys.argv[1])
