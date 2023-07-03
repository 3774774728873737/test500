import socket
from fastapi import FastAPI

app = FastAPI()

@app.get("/api_address")
async def get_api_address():
    """Gets the API address."""
    return {"api_address": socket.gethostbyname(socket.gethostname())}