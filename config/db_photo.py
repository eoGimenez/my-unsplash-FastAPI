import os
from fastapi import HTTPException, status
from schemas.photo import PhotoBase, PhotoDelete
from bson import ObjectId

USER_CODE = os.environ.get('USER_CODE')

NOT_FOUN = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=f'something went wrong'
)


def serializer(photo) -> dict:
    return {
        "_id": str(photo["_id"]),
        "label": str(photo["label"]),
        "imgUrl": str(photo["imgUrl"])
    }


def list_serial(photos) -> list:
    return [serializer(photo) for photo in photos]


def get_all_photos(db):
    try:
        photos = list_serial(db.find())
        return photos
    except:
        raise NOT_FOUN


def post_photo(request: PhotoBase, db) -> dict:
    try:
        created = db.insert_one(dict(request))
        return serializer(db.find_one({"_id": created.inserted_id}))
    except:
        raise NOT_FOUN


def update_one_photo(id: str, request: PhotoBase, db):
    try:
        updated_one = db.find_one_and_update(
            {"_id": ObjectId(id)}, {"$set": dict(request)})
        return serializer(db.find_one({"_id": updated_one["_id"]}))
    except:
        raise NOT_FOUN


def delete_one(id: str, db):
    try:
        db.find_one_and_delete({"_id": ObjectId(id)})
        return {"message": "The Photo was deleted"}
    except:
        raise NOT_FOUN


def get_user_code(request: PhotoDelete):
    if (request.userCode != USER_CODE):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Your User code is not correct'
                            )
    return status.HTTP_100_CONTINUE
