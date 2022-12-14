from fastapi import FastAPI, Depends
from database import engine, Base
from routers import category, report, reportsample
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:8080"
    "https://vast-lake-18728.herokuapp.com",
    "https://vast-lake-18728.herokuapp.com/",
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# Base API Call
@app.get('/')
def hello():
    return {"message": "API Running"}

# Router Include
app.include_router(category.router, tags=['Category'])
app.include_router(report.router, tags=['Report'])
app.include_router(reportsample.router, tags=['ReportSample'])

# Executable
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
