from fastapi import FastAPI, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from io import BytesIO
from dotenv import load_dotenv

import openai
import os


app = FastAPI()

load_dotenv()

# Added OPENAI to the server
client = openai

# Grab API KEY from local enviroment (need to change to env file in future!!!)

client.api_key = os.getenv("OPENAI_API_KEY")



if client.api_key:
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
async def edit_image(request: Request, image: UploadFile = File(...)):
    try:
        image_data = await image.read()

        res = client.images.edit(
            image=image_data,
            n=1,
            size="1024x1024",
            prompt="Edit and enhance this food image to look like a item for a resturant menu."
        )

        edited_image_url = res.get('data')[0]["url"]

        print(edited_image_url)

    except client.error.InvalidRequestError as e:
        return {"error": "Invalid request. Please check your input and try again."}
    except client.error.AuthenticationError:
        return {"error": "Authentication failed. Check your API key."}
    except client.error.RateLimitError:
        return {"error": "Rate limit exceeded. Try again later."}
    except client.error.OpenAIError as e:
        if "billing_hard_limit_reached" in str(e):
            return {"error": "Billing limit reached. Please update your OpenAI account billing settings."}
        return {"error": "An unexpected error occurred: " + str(e)}

     
    
    
    
    


    




# Initializing the home URL (Need to learn how to get to react frontend)
@app.get("/")
async def root():
    return {"message": "Hello from the server!"}


