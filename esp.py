import pymem
import pymem.process
import win32gui
from offset import *
def esp():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    while True:
        glow_manager = pm.read_int(client + dwGlowObjectManager)
        for i in range(1, 32):  # Entities 1-32 are reserved for players.
            entity = pm.read_int(client + EntityList + i * 0x10)
            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)
                if entity_team_id == 2:  # Terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1))  
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))  
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0)) 
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)          
                elif entity_team_id == 3:  # Counter-terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))  
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))  
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1)) 
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1) 
