from ctypes import *

class TickStruct(Structure):
    _pack_ = 1
    _fields_ = [
        ('symbol',c_char*6),
        ('datetime',c_double),
        ('bid',c_double),
        ('ask',c_double)]
    
    def __repr__(self):
        return "Symbol : %s, datetime : %f, bid : %f, ask : %f"%(self.symbol, self.datetime, self.bid, self.ask)