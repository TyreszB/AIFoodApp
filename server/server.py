from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os

app = FastAPI()
client = OpenAI()
api_key = os.environ.get('OPENAI_API_KEY')

if api_key:
    print('API key found!')
    print(api_key)
else:
    print('Error!')

origins = [
    "*"
    ]


image_params = {
    "n": 1,
    "size": "1024x1024",
    "prompt": "Edit and enhance this food image to look like a item for a resturant menu.",

}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def root():
    return {"message": "Hello from the server!"}
