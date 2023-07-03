from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def read_root():
    client_host = Request.client.host
    return {"client_host": client_host}
