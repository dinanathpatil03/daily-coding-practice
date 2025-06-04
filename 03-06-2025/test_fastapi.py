from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the input data model
class BioData(BaseModel):
    name: str
    age: int
    profession: str

@app.get("/")
def get_api():
    return {"message": "Hello World!!"}

@app.get("/{name}")
def get_name(name):
    return {name: "Dinanath Patil"}

# POST endpoint that accepts JSON input
@app.post("/biodata")
def post_biodata(data: BioData):
    return {
        "message": "Data received successfully",
        "data": {
            "name": data.name,
            "age": data.age,
            "profession": data.profession
        }
    }
