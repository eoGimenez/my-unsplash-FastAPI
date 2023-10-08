from pydantic import BaseModel

class PhotoBase(BaseModel):
    label: str
    imgUrl: str

class PhotoDisplay(BaseModel):
    _id: str
    label: str
    imgUrl: str