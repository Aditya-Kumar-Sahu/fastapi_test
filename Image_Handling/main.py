from fastapi import FastAPI, File, UploadFile
from PIL import Image
from uvicorn import run

app = FastAPI()

@app.post("/uploadimage/")
# async def upload_image(image: bytes = File()):
async def upload_image(image: UploadFile = File(media_type="jpg")):
    img = Image.open(image.file)
    img.save("Image_Handling/pic.jpg")
    return {"filename": image.filename}

run(app=app)