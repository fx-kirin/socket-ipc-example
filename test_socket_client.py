import ctypes
from tick_struct import TickStruct
import socket
import time
from benchmarker import Benchmarker

MSGLEN = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 2233))

tick = TickStruct()
resv_size = ctypes.sizeof(tick)
bid = raw_input()
with Benchmarker(width=20) as bench:
    @bench("main")
    def _(bm):
        for _ in range(1000):
            tick.symbol = "USDJPY"
            tick.datetime = time.time()
            tick.bid = float(bid)
            tick.ask = float(bid)
            client.sendall(buffer(tick))
        client.recv(MSGLEN)