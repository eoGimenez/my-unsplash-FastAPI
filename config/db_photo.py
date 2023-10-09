import os
from fastapi import HTTPException, status
from schemas.photo import PhotoBase, PhotoDelete
from bson import ObjectId

USER_CODE = os.environ.get('USER_CODE')

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
        return {"error": "something went wrong"}
    
def update_one_photo(id: str, request: PhotoBase, db):
    try:
        updated_one = db.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(request)})
        print(updated_one)
        return serializer(db.find_one({"_id": updated_one["_id"]}))
    except:
        return {"error": "something went wrong"}
    
def delete_one(id: str, request, db):
    # Validacion del userCode.
    try:
        db.find_one_and_delete({"_id": ObjectId(id)})
        return {"message": "The Photo was deleted"}
    except:
        return {"error": "something went wrong"}

def get_user_code(request: PhotoDelete):
    if (request.userCode != USER_CODE):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Your User code is not correct')