from structures import Broadcast, BroadcastDTO
import os
from websocket import broadcast_action

async def new_broadcast(broadcast: Broadcast):
    print("entered")
    print(broadcast)
    if broadcast.token and broadcast.token==os.getenv("WS_SENDER_KEY"):
        try:
            while True:   
                broadcastDto = BroadcastDTO(**broadcast.model_dump()) 
                
                print(broadcastDto)
                await broadcast_action(broadcastDto)
        except Exception as e:
            print(e)
            pass

