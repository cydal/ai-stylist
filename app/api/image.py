from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from ..crud import save_image_file, create_image, extract_image_tags
from sqlalchemy.orm import Session
from ..dependencies import get_db
from .. import schemas, crud

image_router = APIRouter()

@image_router.post("/upload")
async def upload_image(user_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(('.png', '.jpg', '.jpeg')):
        raise HTTPException(status_code=400, detail="Invalid file format")

    image_data = await file.read()
    image_path = save_image_file(user_id, image_data, file.filename)
    tags = extract_image_tags(image_path)

    image_record = create_image(db, user_id=user_id, image_path=image_path, tags=tags)
    return image_record

@image_router.get("/{user_id}")
def get_images(user_id: int, db: Session = Depends(get_db)):
    return crud.get_images_by_user(db=db, user_id=user_id)
