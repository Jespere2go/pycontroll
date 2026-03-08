# import asyncore
import json
import socket

CONNECTION_KEY = "test"
server_ip = "127.0.0.1"
port = 9999


# Defines atributes of Client class
class Client:
    def __init__(self, name, ip, overule_shutdown, down_time, up_time):
        self.name = name
        self.ip = ip
        self.overule_shutdown = overule_shutdown
        self.down_time = down_time
        self.up_time = up_time


# Clients is a container for the client objects
class Clients:
    pass


# Loads the json file
with open("clients_conf.json", "r") as f:
    data = json.load(f)

clients = Clients()

# Converts json entries into objects e.g. clients.pve1
for c in data["clients"]:
    client = Client(**c)
    setattr(clients, client.name, client)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((server_ip, port))

while True:
    try:
        while True:
            data, addr = s.recvfrom(1024)
            if (data.decode()) == CONNECTION_KEY:
                s.sendto("repsonse_test".encode(), addr)
            else:
                s.sendto("Please send valid request!".encode(), addr)
    except ConnectionResetError:
        print("Connectin reset!")
