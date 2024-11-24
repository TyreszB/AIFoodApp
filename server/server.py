from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from io import BytesIO

import openai
import os


app = FastAPI()


# Grab API KEY from local enviroment (need to change to env file in future!!!)

openai.api_key = os.getenv("OPENAI_API_KEY")

# Added OPENAI to the server
client = openai


if openai.api_key:
    print('API key found!')
else:
    print('Error!')


# Server allows all URLs to access server (need to change in the future to more secure URL)
origins = [
    "*"
    ]

# Middleware decloration for all headers and methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Parameters for request to OPENAI to edit images (Need learn to add images to params for editing)
image_params = {
    "n": 1,
    "size": "1024x1024",
    "prompt": "Edit and enhance this food image to look like a item for a resturant menu.",

}

# Generate image from OPENAI
@app.post('/api/edit-image')
async def edit_image(request: Request):
    data = await request.json()
    
    print(data)


    




# Initializing the home URL (Need to learn how to get to react frontend)
@app.get("/")
async def root():
    return {"message": "Hello from the server!"}


