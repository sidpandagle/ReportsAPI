from fastapi import FastAPI, Depends
from models import Base
from database import engine, SessionLocal, get_db
from routers import category

import uvicorn

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Base API Call
@app.get('/')
def hello():
    return {"message": "API Running"}

# Router Include
app.include_router(category.router)

# Executable
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
