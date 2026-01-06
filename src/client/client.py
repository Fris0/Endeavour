from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from agents import agent

app = FastAPI()
a = agent.Agent()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse("templates/base.html")

@app.websocket("/ws")
async def entrypoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        response = await a.logic(data)
        await websocket.send_text(response)