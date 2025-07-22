from structures import Broadcast, BroadcastDTO
import os
from WsManager import WsManager
import traceback
async def new_broadcast(broadcast: Broadcast):
    if broadcast.token and broadcast.token==os.getenv("WS_SENDER_KEY"):
        try:
            broadcastDto = BroadcastDTO(**broadcast.model_dump())                 
            await WsManager.broadcast_action(broadcastDto)
        except:
            traceback.print_exc()

