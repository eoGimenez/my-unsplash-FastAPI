import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import photo

app = FastAPI(
    title='Desafio devchallenges.io',
    description='My-Unsplash-master, server versión con FastAPI'
)

ORIGIN = os.environ.get('ORIGIN')

app.add_middleware(
    CORSMiddleware,
    allow_origins= [ORIGIN],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
    expose_headers=['*']
)

app.include_router(photo.router)
