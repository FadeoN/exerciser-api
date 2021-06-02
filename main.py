import uvicorn
from fastapi import FastAPI

from src.infrastucture.configuration import APP_OPTIONS
from src.infrastucture.router import api_router
from src.application import repository

app = FastAPI(
    name=APP_OPTIONS.project_name,
    description="",
    version="1.0.0"
)

app.add_event_handler("startup", repository.connect_db)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5006, workers=1, debug=False)