from fastapi import FastAPI, Request, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import io
from io import BytesIO
from dotenv import load_dotenv
from PIL import Image

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


# Generate image from OPENAI
@app.post('/api/edit-image')
async def edit_image(request: Request, image: UploadFile = File(...)):
    
    try:
        image_bytes = await image.read()

        with Image.open(io.BytesIO(image_bytes)) as img:

            if img.mode != "RGBA":
                img = img.convert("RGBA")

            
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            buffer.seek(0)
            image_bytes = buffer.read()

            if len(image_bytes) > 4 * 1024 * 1024:  # 4 MB
                img.thumbnail((img.width // 2, img.height // 2))
                buffer = io.BytesIO()
                img.save(buffer, format="PNG")
                buffer.seek(0)
                image_bytes = buffer.read()


        res = client.images.edit(
            image=image_bytes,
            n=1,
            prompt="Edit and enhance this food image to look like a item for a resturant menu."
        )
        
        
        edited_image_url = res

        print(edited_image_url)

        

# Error handling for post request to OPENAI
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


