from fastapi import FastAPI, Depends
from database import engine, Base
from routers import category, report

import uvicorn

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Base API Call
@app.get('/')
def hello():
    return {"message": "API Running"}

# Router Include
app.include_router(category.router, tags=['Category'])
app.include_router(report.router, tags=['Report'])

# Executable
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
