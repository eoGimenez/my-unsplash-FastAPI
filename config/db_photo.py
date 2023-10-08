from fastapi import HTTPException, status
from schemas.photo import PhotoBase
from bson import ObjectId

def serializer(photo) -> dict:
    return {
        "_id": str(photo["_id"]),
        "label": str(photo["label"]),
        "imgUrl": str(photo["imgUrl"])
    }

def list_serial(photos) -> list:
    return [serializer(photo) for photo in photos]

def get_all_photos(db):
    photos = list_serial(db.find())
    return photos

def post_photo(request: PhotoBase, db):
    try:
        created = db.insert_one(dict(request))
        return serializer(db.find_one({"_id": created.inserted_id}))
    except:
        return {"message": "something went wrong"}
    
def update_one_photo(id: str, request: PhotoBase, db):
    try:
        updated_one = db.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(request)})
        return serializer(db.find_one({"_id": updated_one["_id"]}))
    except:
        return {"message": "something went wrong"}