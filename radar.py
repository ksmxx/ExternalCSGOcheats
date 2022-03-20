import pymem
import pymem.process
import win32gui
from offset import *
def radar():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    while True:
        glow_manager = pm.read_int(client + dwGlowObjectManager)
        for i in range(1, 32): 
            entity = pm.read_int(client + EntityList + i * 0x10)
            if entity:
                pm.write_uchar(entity + m_bSpotted, 1)
