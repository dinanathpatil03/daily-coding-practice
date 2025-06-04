from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

all_data = []

class biodata(BaseModel):
    name: str
    age: int
    profession: str

@app.get("/get_all_data")
def get_details():
    return {"all_details": all_data}

@app.post("/data")
def post_details(details:biodata):
    all_data.append(details)
    return {"message": "Data has been successfully stores.",
            "details": details
    }

@app.delete("/delete/{name}")
def delete_details(name: str):
    for item in all_data:
        if item.name == name:
            all_data.remove(item)
            return {"message": f"Data for {name} deleted successfully."}
    
    raise HTTPException(status_code=404, detail="Data not found")













