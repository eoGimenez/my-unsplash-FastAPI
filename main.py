from fastapi import FastAPI
from routes import photo

app = FastAPI()


app.include_router(photo.router)
