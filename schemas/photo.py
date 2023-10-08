from pydantic import BaseModel, Field

class PhotoBase(BaseModel):
    label: str
    imgUrl: str

class PhotoDisplay(BaseModel):
    id: str = Field(alias="_id")
    label: str
    imgUrl: str

class PhotoDelete(BaseModel):
    userCode: str