from fastapi import FastAPI

app = FastAPI


@app.get("/items/{item_id")
async def read_items(item_id):
    return {"item_id": item_id}