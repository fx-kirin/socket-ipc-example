import socket
import select
import ctypes
from tick_struct import TickStruct

MSGLEN = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("localhost", 2233))
server.listen(1)
client, client_address = server.accept()

print "Socket server started"
tick = TickStruct()
resv_size = ctypes.sizeof(tick)
count = 0
while True:
    r, w, e = select.select([client], [], [])
    for reader in r:
        reader.recv_into(tick)
        print tick
        count += 1
        
    if(count >= 1000):
        client.sendall("finish")
        break