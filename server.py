# import asyncore
# import json
import socket

server_ip = "127.0.0.1"
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data, addr = s.recvfrom(1024)
    print(data.decode())
    s.sendto(f"Data to client {addr}".encode(), addr)
