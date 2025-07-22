from pydantic import BaseModel
from typing import List

class Macro(BaseModel):
    name: str
    time_started: str

class Broadcast(BaseModel):
    token: str
    status: str
    macros_running: List[Macro]
    
class BroadcastDTO(BaseModel):
    status: str = ""
    macros_running: List[Macro] = []