from fastapi import FastAPI
from app.streaming.ws_echo import router as ws_router

app = FastAPI(title="AI Voice Demo Engine")

@app.get("/")
async def root():
    return {"status": "ok", "service": "ai-voice-demo-engine"}

# Minimal WS endpoint to prove streaming works end-to-end
app.include_router(ws_router)
