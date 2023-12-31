from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def read_root():
    request: Request = app.state.request
    client_host = request.client.host
    return {"client_host": client_host}
