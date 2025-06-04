from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # rename here

class data(BaseModel):
    name: str
    age: int
    address: str

@app.get("/{name}")
def get_data(name):
    return {"message": name}

@app.post("/biodata")
def post_data(data: data):
    return {
        "message": "Successfully data has been stored",
        "data": {
            "name": data.name,
            "age": data.age,
            "address": data.address
        }
    }

