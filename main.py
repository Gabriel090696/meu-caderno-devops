import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return dict(teste=True, num_aleatorio=random.randint(1, 100))
