from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.utils.logging import get_logger

router = APIRouter()
log = get_logger(__name__)

@router.websocket("/ws/echo")
async def ws_echo(ws: WebSocket):
    await ws.accept()
    log.info("ws_connected")
    try:
        while True:
            msg = await ws.receive_text()
            # Minimal placeholder: echo back
            await ws.send_text(f"echo: {msg}")
    except WebSocketDisconnect:
        log.info("ws_disconnected")
