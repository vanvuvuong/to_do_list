from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return "Hello World"

async def add_item():
    # get item from POST body