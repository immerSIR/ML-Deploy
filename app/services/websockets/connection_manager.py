from fastapi import FastAPI, WebSocket
import json


class ConnectionManager:
    
    def __init__(self)-> None:
        self.active_connections: List[WebSocket] = []
        
    async def connect(self, websocket:WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        
    def disconnect(self, websocket:WebSocket):
        self.active_connections.remove(websocket)
        
    
    async def send_message(self, message:json, websocket:WebSocket):
        await websocket.send_json(message)
        
    async def broadcast(self, message:json):
        for connection in self.active_connections:
            await connection.send_json(message)
            