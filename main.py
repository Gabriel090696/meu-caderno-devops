from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def  root():
    return {"Hello": "World"}

@app.get("/teste1")
async def funcaoteste():
    return {"teste": "deu certo"}