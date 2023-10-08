from fastapi import APIRouter
from schemas.photo import PhotoBase, PhotoDisplay
from typing import List

router = APIRouter(prefix='/api')

@router.get('/', response_model=List[PhotoDisplay])
async def get_all_photos():
    pass

@router.post('/', response_model=PhotoDisplay)
async def post_new_photo(request: PhotoBase):
    pass