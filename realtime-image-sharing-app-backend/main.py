from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

import facedetect;

app = FastAPI()

class Image(BaseModel):
    id: int
    name: str
    url: str

images: List[Image] = [
    Image(id=1, name="Image 1", url="./img1.png"),
    Image(id=2, name="Image 2", url="./img2.png"),
    Image(id=3, name="Image 3", url="./img3.png"),
    Image(id=4, name="Image 4", url="./img4.png"),
    Image(id=5, name="Image 5", url="./im5png"),
]

@app.get("/images", response_model=List[Image])
def get_images():
    return images

@app.get("/images/{image_id}", response_model=Optional[Image])
def get_image(image_id: int):
    image = next((image for image in images if image.id == image_id), None)
    return image

@app.post("/images/create", response_model=Image)
def create_image(image: Image):
    images.append(image)
    return image

@app.put("/images/update/{image_id}", response_model=Optional[Image])
def update_image(image_id: int, updated_image: Image):
    image = next((image for image in images if image.id == image_id), None)
    if image:
        image.name = updated_image.name
        image.url = updated_image.url
        return image
    else:
        return None

@app.delete("/images/delete/{image_id}")
def delete_image(image_id: int):
    global images
    images = [image for image in images if image.id != image_id]
    return {"detail": "Image deleted"}