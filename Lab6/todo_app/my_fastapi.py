from fastapi import FastAPI, Path, Query

app = FastAPI()


# GET REST API
@app.get("/items/")
async def get_items():
    return {"message": "GET request to /items/"}


# GET REST API with Path Parameter
@app.get("/items/{item_id}")
async def get_item(item_id: int = Path(..., title="The ID of the item")):
    return {"message": f"GET request to /items/{item_id}"}


# GET REST API with Query Parameters
@app.get("/items/query/")
async def get_items_with_query_params(skip: int = Query(0, title="Skip items"),
                                      limit: int = Query(10, title="Limit items")):
    return {"message": f"GET request to /items/query/?skip={skip}&limit={limit}"}


# GET REST API with Path Parameters AND Query Parameters
@app.get("/items/{item_id}/details")
async def get_item_with_query_params(
        item_id: int = Path(..., title="The ID of the item"),
        skip: int = Query(0, title="Skip items"),
        limit: int = Query(10, title="Limit items")
):
    return {"message": f"GET request to /items/{item_id}/details?skip={skip}&limit={limit}"}


# POST REST API
@app.post("/items/")
async def create_item(item: dict):
    return {"message": "POST request to /items/", "item": item}


# PUT REST API
@app.put("/items/{item_id}")
async def update_item(item: dict, item_id: int = Path(..., title="The ID of the item")):
    return {"message": f"PUT request to /items/{item_id}", "updated_item": item}


# DELETE REST API
@app.delete("/items/{item_id}")
async def delete_item(item_id: int = Path(..., title="The ID of the item")):
    return {"message": f"DELETE request to /items/{item_id}"}
