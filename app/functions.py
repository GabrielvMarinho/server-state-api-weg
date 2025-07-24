from structures import Broadcast, BroadcastFinishMacro, BroadcastFinishAllMacro
import os
from WsManager import WsManager
import traceback

async def remove_all_and_broadcast(broadcast :BroadcastFinishAllMacro):
    if is_token_valid(broadcast.token):
        await WsManager.remove_all_from_state()
    else:
        {"status":"fail", "error":"Not valid token"}
        
async def remove_and_broadcast(broadcast :BroadcastFinishMacro):
    if is_token_valid(broadcast.token):
        try:
            await WsManager.remove_from_state(broadcast.id)          
            await WsManager.broadcast_new_state()

            return {"status":"success"}
        except:
            err = traceback.print_exc()
            return {"status":"fail", "error":err}
    else:
        {"status":"fail", "error":"Not valid token"}
        

async def add_and_broadcast(broadcast :Broadcast):
    if is_token_valid(broadcast.token):
        try:
            await WsManager.add_to_state(broadcast.macro)          
            await WsManager.broadcast_new_state()
            return {"status":"success"}
        except:
            err = traceback.print_exc()
            return {"status":"fail", "error":err}
    else:
        {"status":"fail", "error":"Not valid token"}

def is_token_valid(token):
    if token and token==os.getenv("WS_SENDER_KEY"):
        return True
    return False