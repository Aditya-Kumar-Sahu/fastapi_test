from typing import Union

from fastapi import FastAPI, Query

from uvicorn import run

app = FastAPI()


@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=...,min_length=5, max_length=20)):
    results = {"items": [{"item_id": "Foo"}, {"ittem_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


run(app=app)