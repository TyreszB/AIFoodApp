from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os

app = FastAPI()

# Added OPENAI to the server
client = OpenAI()

# Grab API KEY from local enviroment (need to change to env file in future!!!)
api_key = os.environ.get('OPENAI_API_KEY')

if api_key:
    print('API key found!')
else:
    print('Error!')


# Server allows all URLs to access server (need to change in the future to more secure URL)
origins = [
    "*"
    ]

# Parameters for request to OPENAI to edit images (Need learn to add images to params for editing)
image_params = {
    "n": 1,
    "size": "1024x1024",
    "prompt": "Edit and enhance this food image to look like a item for a resturant menu.",

}

# Middleware decloration for all headers and methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initializing the home URL (Need to learn how to get to react frontend)
@app.get("/")
async def root():
    return {"message": "Hello from the server!"}
