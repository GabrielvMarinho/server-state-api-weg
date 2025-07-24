from pydantic import BaseModel
from typing import List

class MacroPost(BaseModel):
    id: str
    name: str
    
class MacroResponse(BaseModel):
    id: str
    name: str
    time_started: str

class Broadcast(BaseModel):
    token: str
    macro: MacroPost

class BroadcastFinishMacro(BaseModel):
    token: str
    id: str

class BroadcastFinishAllMacro(BaseModel):
    token: str
