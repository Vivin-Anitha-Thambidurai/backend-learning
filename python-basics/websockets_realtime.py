"""
websockets_realtime.py

Demonstrates real-time communication using WebSockets in FastAPI.
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI(title="WebSockets Real-Time Example")


# ------------------------
# Connection manager
# ------------------------

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


# ------------------------
# WebSocket endpoint
# ------------------------

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast("A client disconnected ❌")


# ------------------------
# HTTP route
# ------------------------

@app.get("/")
def root():
    return {"message": "WebSocket server running 🚀"}
