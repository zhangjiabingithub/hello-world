import os
import sys
import SComSocket
from enum import Enum
class Week(Enum):
    SOCKET = 1
    
def run():
    print("dd")
a = SComSocket.SComSocket()
a.init("socketTest","127.0.0.1","7600")
# a.open()
a.writeString("ssss")