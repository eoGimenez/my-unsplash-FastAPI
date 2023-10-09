
from fastapi import APIRouter, Depends, Security
from schemas.photo import PhotoBase, PhotoDisplay, PhotoDelete
from typing import List
from config.database import get_db
from config import db_photo

router = APIRouter(prefix='/api')



@router.get('/', response_model=List[PhotoDisplay])
async def get_photos(db = Depends(get_db)):
    return db_photo.get_all_photos(db)
    

@router.post('/', response_model=PhotoDisplay)
async def new_photo(request: PhotoBase, db = Depends(get_db)):
    return db_photo.post_photo(request, db)

@router.put('/{id}', response_model=PhotoDisplay)
async def update_photo(id: str, request: PhotoBase, db = Depends(get_db)):
    return db_photo.update_one_photo(id, request, db)

@router.delete('/{id}')
async def delete_photo(id: str, request: PhotoDelete = Security(db_photo.get_user_code), db = Depends(get_db)):
    return db_photo.delete_one(id, request, db)