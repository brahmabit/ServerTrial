import socket
import threading
import sys
import os.path
import base64
import os
import FileManager

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(('0.0.0.0', 8080))

        self.sock.listen(1)


    def handler(self,c, a):
        #global connections
        counter = 0

        while True:
            data = c.recv(81920000)
            for connection in self.connections:
                counter+=1;
                #hel = pallindrome.pall(str(data, 'utf-8'))
                #Database.databaseStore(str(data, 'utf-8'),hel)
                #connection.send(hel.encode())
                #print(str(data, 'utf-8'))
                check = FileManager.storeImage(data,"image{}.jpeg".format(counter))
                print(check)
                #ImageName = "trial2.jpeg"
                #save_path = 'D:/ServerTrial/images'
                ##completename = os.path.join(save_path, ImageName)
                #data1 = base64.b64decode(data)
            #    data = str(data, 'utf-8')
            #    if len(data) % 4 != 0: #check if multiple of 4
                #    while len(data) % 4 != 0:
                #        data = data + "="
                #    data = data.encode()
            #        req_str = base64.b64decode(data)
            #    else:
            #        req_str = base64.b64decode(data)

            #    image_result = open(completename, 'wb') # create a writable image and write the decoding result
            #    image_result.write(data1)
            #    image_result.close()
                #Database.databaseStore("trial",check)
                connection.send("\nSuccessful\n".encode())
            if not data:
                print(str(a[0])+':'+str(a[1]), "disconnected")
                self.connections.remove(c)
                c.close()
                break

    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c,a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0])+':'+str(a[1]), "connected")


server = Server()
server.run()
