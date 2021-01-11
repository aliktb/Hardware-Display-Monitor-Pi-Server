#Imports modules
import socket
import time
import threading

mylist = [0,0,0,0,0,0,0,0]

listensocket = socket.socket() #Creates an instance of socket
Port = 8000 #Port to host server on
maxConnections = 999
IP = socket.gethostname() #IP address of local machine

listensocket.bind(('',Port))

#Starts server
listensocket.listen(maxConnections)
print("Server started at " + IP + " on port " + str(Port))

#Accepts the incomming connection
(clientsocket, address) = listensocket.accept()
print("New connection made!")

#decodes incoming message and places values in mylist
def tcp_in():

    global mylist

    while True:

        try:

            message = clientsocket.recv(1024).decode() #Gets the incomming message

            #while (message.strip()) != "[":
            #    pass

            mylist = message.split(",")



        except:
    #  print(message)
            pass

        time.sleep(0.1)


t = threading.Thread(target =tcp_in)
t.start()

def cpu_load():
    global mylist
    return float(mylist[0])

def cpu_temperature():
    global mylist
    return float(mylist[1])

def gpu_load():
    global mylist
    return float(mylist[2])

def gpu_temperature():
    global mylist
    return float(mylist[3])

def RAM_load():
    global mylist
    return float(mylist[4])

def front_fan():
    global mylist
    return float(mylist[5])

def cpu_fan():
    global mylist
    return float(mylist[6])

def rear_fan():
    global mylist
    return float(mylist[7])
